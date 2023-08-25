#include <algorithm>
#include <array>
#include <bit>
#include <cstring>
#include <numeric>
#include <random>
#include <stdexcept>
#include <cassert>

#include "benchmark/benchmark.h"
#include "common.hpp"
#include "config.h"
#include "simd.hpp"
#include <iostream>

#define assertm(exp, msg) assert(((void)msg, exp))

using RowId = uint32_t;
using KEYVAL = uint32_t;

// 64bit alignment of 32 bit values.
// This is to help the SIMDizer
using KEYCOL = AlignedData<KEYVAL, 64>;
using MatchingRows = AlignedData<RowId, 64>;


/*
 * Builds a lookup table that, given a comparison-result bitmask, returns the indices of the matching elements
 * compressed to the front. Can be used as a shuffle mask for source-selecting shuffles. Examples:
 * [0 0 0 1] -> [0, unused_index, unused_index, unused_index]
 * [1 0 1 0] -> [1, 3, unused_index, unused_index]
 */
template <size_t ComparisonResultBits, typename IndexT, IndexT unused_index>
static constexpr auto lookup_table_for_compressed_offsets_by_comparison_result() {
  std::array<std::array<IndexT, ComparisonResultBits>, 1 << ComparisonResultBits> lookup_table{};

  for (size_t index = 0; index < lookup_table.size(); ++index) {
    auto& shuffle_mask = lookup_table[index];
    std::fill(shuffle_mask.begin(), shuffle_mask.end(), unused_index);

    size_t first_empty_output_slot = 0;
    for (size_t comparison_result_rest = index; comparison_result_rest != 0;
         comparison_result_rest &= comparison_result_rest - 1) {
      shuffle_mask[first_empty_output_slot++] = std::countr_zero(comparison_result_rest);
    }
  }

  return lookup_table;
}

/*
 * SSE and NEON do not allow shuffling elements with run-time masks, so we have to create byte shuffle masks.
 * This transforms a shuffle mask like [1, 3, unused_index, unused_index] for `uint32_t`s to the byte mask
 * [4, 5, 6, 7,   12, 13, 14, 15,   U, U, U, U,   U, U, U, U ]
 */
template <typename VectorElementT, typename IndexT, IndexT unused_index>
static constexpr auto element_shuffle_table_to_byte_shuffle_table(auto element_shuffle_table) {
  static_assert(std::endian::native == std::endian::little, "Probably doesn't work for big-endian systems.");
  constexpr size_t OUTPUT_ELEMENTS_PER_MASK = sizeof(VectorElementT) * element_shuffle_table[0].size();
  std::array<std::array<IndexT, OUTPUT_ELEMENTS_PER_MASK>, element_shuffle_table.size()> byte_shuffle_table{};

  for (size_t row = 0; row < element_shuffle_table.size(); ++row) {
    const auto& element_shuffle_mask = element_shuffle_table[row];
    auto& byte_shuffle_mask = byte_shuffle_table[row];

    for (size_t element_index = 0; element_index < element_shuffle_mask.size(); ++element_index) {
      const auto element_mask_value = element_shuffle_mask[element_index];
      IndexT* byte_mask_group_begin = byte_shuffle_mask.data() + element_index * sizeof(VectorElementT);
      IndexT* byte_mask_group_end = byte_mask_group_begin + sizeof(VectorElementT);

      if (element_mask_value == unused_index) {
        std::fill(byte_mask_group_begin, byte_mask_group_end, unused_index);
      } else {
        std::iota(byte_mask_group_begin, byte_mask_group_end, element_mask_value * sizeof(VectorElementT));
      }
    }
  }

  return byte_shuffle_table;
}

struct naive_scan {
  RowId operator()(const KEYCOL& Lo, const KEYCOL& Hi, KEYVAL filter_val, MatchingRows* matching_rows) {
    const KEYVAL* High = Hi.aligned_data();
    const KEYVAL* Low = Lo.aligned_data();
    RowId* output = matching_rows->aligned_data();

    RowId num_matching_rows = 0;
    for (RowId row = 0; row < NUM_ROWS; ++row) {
      if (High[row] > filter_val && Low[row] < filter_val) {
        output[num_matching_rows++] = row;
      }
    }
    return num_matching_rows;
  }
};

struct autovec_scan {
  RowId operator()(const KEYCOL& Lo, const KEYCOL& Hi, KEYVAL filter_val, MatchingRows* matching_rows) {
    // The naive version should be autovectorizable with clang, but they currently don't do this
    // see https://github.com/llvm/llvm-project/issues/42210
    // According to the issue, ICC can autovectorize this.
    // Godbolt playground: https://godbolt.org/z/aahTPczdr

    const KEYVAL* __restrict High = Hi.aligned_data();
    const KEYVAL* __restrict Low = Lo.aligned_data();

    RowId* __restrict output = matching_rows->aligned_data();

    RowId num_matching_rows = 0;
    for (RowId row = 0; row < NUM_ROWS; ++row) {
      output[num_matching_rows] = row;
      num_matching_rows += static_cast<int>(High[row] > filter_val && Low[row] < filter_val);
    }
    return num_matching_rows;
  }
};

struct vector_128_scan_predication {
  using DictVec = simd::GccVec<KEYVAL, 16>::T;
  static constexpr size_t NUM_MATCHES_PER_VECTOR = sizeof(DictVec) / sizeof(KEYVAL);

  RowId operator()(const KEYCOL& Lo, const KEYCOL& Hi, KEYVAL filter_val, MatchingRows* matching_rows) {
    RowId num_matching_rows = 0;

    const KEYVAL* __restrict lows = Lo.aligned_data();
    const KEYVAL* __restrict highs = Hi.aligned_data();

    RowId* __restrict output = matching_rows->aligned_data();

    static_assert(NUM_ROWS % (NUM_MATCHES_PER_VECTOR) == 0);
    for (RowId chunk_start_row = 0; chunk_start_row < NUM_ROWS; chunk_start_row += NUM_MATCHES_PER_VECTOR) {
      const auto lows_to_match = simd::load<DictVec>(lows + chunk_start_row);
      const auto highs_to_match = simd::load<DictVec>(highs + chunk_start_row);

      const DictVec matches = lows_to_match < filter_val & highs_to_match > filter_val;
      for (RowId row = 0; row < NUM_MATCHES_PER_VECTOR; ++row) {
        output[num_matching_rows] = chunk_start_row + row;
        num_matching_rows += matches[row] & 1u ;
      }
    }
    return num_matching_rows;
  }
};

template <typename ScanFn>
void BM_dictionary_scan(benchmark::State& state) {
  {
    KEYCOL Lo{NUM_ROWS};
    KEYCOL Hi{NUM_ROWS};

    MatchingRows matching_rows{NUM_ROWS};

    static_assert(NUM_ROWS % NUM_UNIQUE_VALUES == 0, "Number of rows must be a multiple of num unique values.");
    const int64_t input_percentage = state.range(0);
    const auto percentage_to_pass_filter = static_cast<double>(input_percentage) / 100;

    // Our filter value comparison is `row < filter_value`, so we can control the selectivity as follows:
    //   For percentage =   0, the filter value is                     0, i.e., no values will match.
    //   For percentage =  50, the filter value is NUM_UNIQUE_VALUES / 2, i.e., 50% of all values will match.
    //   For percentage = 100, the filter value is     NUM_UNIQUE_VALUES, i.e., all values will match.
    const auto filter_value = static_cast<KEYVAL>(NUM_UNIQUE_VALUES * percentage_to_pass_filter);

    KEYVAL* Low = Lo.aligned_data();
    KEYVAL* High = Hi.aligned_data();

    for (size_t i = 0; i < NUM_ROWS; ++i) {
      Low[i] = i % NUM_UNIQUE_VALUES;
    }
    std::mt19937 rng{std::random_device{}()};
    std::shuffle(Low, Low + NUM_ROWS, rng);

    for (size_t i = 0; i < NUM_ROWS; ++i) {
      High[i] = Low[i] + i % NUM_UNIQUE_VALUES;
    }

    // Correctness check with naive implementation
    ScanFn scan_fn{};
    MatchingRows matching_rows_naive{NUM_ROWS};
    const RowId num_matches_naive = naive_scan{}(Lo, Hi, filter_value, &matching_rows_naive);
    const RowId num_matches_specialized = scan_fn(Lo, Hi, filter_value, &matching_rows);

    if (num_matches_naive != num_matches_specialized) {
      throw std::runtime_error{"Bad result. Expected " + std::to_string(num_matches_naive) +
                               " rows to match, but got " + std::to_string(num_matches_specialized)};
    }
    for (size_t i = 0; i < num_matches_naive; ++i) {
      if (matching_rows_naive.aligned_data()[i] != matching_rows.aligned_data()[i]) {
        throw std::runtime_error{"Bad result compare at position: " + std::to_string(i)};
      }
    }

    // Print Lo and Hi of matching rows
    // std::cout << "Filter Value" << filter_value << std::endl;
    // for (size_t i = 0; i < num_matches_naive; ++i) {
    //   std::cout << "Lo: " << Low[matching_rows_naive.aligned_data()[i]]
    //             << " Hi: " << High[matching_rows_naive.aligned_data()[i]] << std::endl;
    // }

    // Sanity check that the 100 and 0 percent math works out.
    if (input_percentage == 100 && num_matches_specialized != NUM_ROWS) {
      throw std::runtime_error{"Bad result. Did not match all rows."};
    }
    if (input_percentage == 0 && num_matches_specialized != 0) {
      throw std::runtime_error{"Bad result. Did not match 0 rows."};
    }

    benchmark::DoNotOptimize(Lo.aligned_data());
    benchmark::DoNotOptimize(matching_rows.aligned_data());

    for (auto _ : state) {
      const RowId num_matches = scan_fn(Lo, Hi, filter_value, &matching_rows);
      // std::cout << "matches" << num_matches << std::endl;
      benchmark::DoNotOptimize(num_matches);
    }

    state.counters["PerValue"] = benchmark::Counter(static_cast<double>(state.iterations() * NUM_ROWS),
                                                    benchmark::Counter::kIsRate | benchmark::Counter::kInvert);
  }
}

template <size_t VECTOR_SIZE_IN_BYTES, typename RowOffsetT>
struct vector_scan_add {
  using VecT = typename simd::GccVec<KEYVAL, VECTOR_SIZE_IN_BYTES>::T;
  static constexpr size_t NUM_VECTOR_ELEMENTS =
      VECTOR_SIZE_IN_BYTES / sizeof(KEYVAL);
  using RowOffsetVecT =
      typename simd::GccVec<RowOffsetT,
                            NUM_VECTOR_ELEMENTS * sizeof(RowOffsetT)>::T;

  alignas(VECTOR_SIZE_IN_BYTES) static constexpr std::array<
      std::array<RowOffsetT, NUM_VECTOR_ELEMENTS>,
      1 << NUM_VECTOR_ELEMENTS> MATCHES_TO_ROW_OFFSETS =
      lookup_table_for_compressed_offsets_by_comparison_result<
          NUM_VECTOR_ELEMENTS, RowOffsetT, 0>();

  // Haswell is a bit slower here because LLVM generates the comparison and
  // move-to-mask inefficiently, see https://godbolt.org/z/bzrxb57Kh This does
  // not occur on more modern architectures.
  RowId operator()(const KEYCOL &Lo, const KEYCOL &Hi, KEYVAL filter_val,
                   MatchingRows *matching_rows) {
    const KEYVAL *__restrict lows = Lo.aligned_data();
    const KEYVAL *__restrict highs = Hi.aligned_data();
    RowId *__restrict output = matching_rows->aligned_data();

    RowId num_matching_rows = 0;
    static_assert(NUM_ROWS % NUM_VECTOR_ELEMENTS == 0);

    for (RowId chunk_start_row = 0; chunk_start_row < NUM_ROWS;
         chunk_start_row += NUM_VECTOR_ELEMENTS) {
      const VecT low_values = simd::load<VecT>(lows + chunk_start_row);
      const VecT high_values = simd::load<VecT>(highs + chunk_start_row);
      
      
      const VecT compare_result = low_values < filter_val & high_values > filter_val;
      
      const unsigned int packed_compare_result =
          simd::comparison_to_bitmask<VecT>(compare_result);

      const auto matching_row_offsets = simd::load<RowOffsetVecT>(
          MATCHES_TO_ROW_OFFSETS[packed_compare_result].data());
      const VecT compressed_matching_rows =
          chunk_start_row + __builtin_convertvector(matching_row_offsets, VecT);

      simd::store_unaligned(output + num_matching_rows,
                            compressed_matching_rows);
      num_matching_rows += std::popcount(packed_compare_result);
    }
    return num_matching_rows;
  }
};