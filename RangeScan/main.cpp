#include "range_scan.hpp"

using vector_128_scan_add = vector_scan_add<16, uint32_t>;
// using uint8_t as RowOffsetT didn't give a measurable performance boost on
// icelake, but it decreases GCC performance
using vector_256_scan_add = vector_scan_add<32, uint32_t>;

int main() {
  // Range tag arrays. We use column store for the Lo and Hi tags to enable SIMD
  // loads; otherwise we would have to unpack them
  KEYCOL Lo{NUM_ROWS};
  KEYCOL Hi{NUM_ROWS};

  // Where the results would be stored. Here we assume that all entries might
  // match. In practice, we would have to estimate the number of matches based
  // on levels in IDX.
  MatchingRows matching_rows{NUM_ROWS};

  static_assert(NUM_ROWS % NUM_UNIQUE_VALUES == 0,
                "Number of rows must be a multiple of num unique values.");

////////////////////////////////////////////////////////////////////////////////
//             Create input dataset
////////////////////////////////////////////////////////////////////////////////
  /**
   * @brief Create input dataset.
   * input_percentage controls the number of potential matches.
   */
  const int64_t input_percentage = 50;

  const auto percentage_to_pass_filter =
      static_cast<double>(input_percentage) / 100;

  // Our filter value comparison is `row < filter_value`, so we can control the
  // selectivity as follows:
  //   For percentage =   0, the filter value is                     0, i.e., no
  //   values will match. For percentage =  50, the filter value is
  //   NUM_UNIQUE_VALUES / 2, i.e., 50% of all values will match. For percentage
  //   = 100, the filter value is     NUM_UNIQUE_VALUES, i.e., all values will
  //   match.
  const auto filter_value =
      static_cast<KEYVAL>(NUM_UNIQUE_VALUES * percentage_to_pass_filter);

  KEYVAL *Low = Lo.aligned_data();
  KEYVAL *High = Hi.aligned_data();

  for (size_t i = 0; i < NUM_ROWS; ++i) {
    Low[i] = i % NUM_UNIQUE_VALUES;
  }
  std::mt19937 rng{std::random_device{}()};
  std::shuffle(Low, Low + NUM_ROWS, rng);

  for (size_t i = 0; i < NUM_ROWS; ++i) {
    High[i] = Low[i] + i % NUM_UNIQUE_VALUES;
  }
  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  // Correctness check with naive implementation
  MatchingRows matching_rows_naive{NUM_ROWS};
  const RowId num_matches_naive =
      naive_scan{}(Lo, Hi, filter_value, &matching_rows_naive);

  //   SIMD matches
  const RowId num_matches_specialized =
      vector_128_scan_add{}(Lo, Hi, filter_value, &matching_rows);

  if (num_matches_naive != num_matches_specialized) {
    throw std::runtime_error{
        "Bad result. Expected " + std::to_string(num_matches_naive) +
        " rows to match, but got " + std::to_string(num_matches_specialized)};
  }
  for (size_t i = 0; i < num_matches_naive; ++i) {
    if (matching_rows_naive.aligned_data()[i] !=
        matching_rows.aligned_data()[i]) {
      throw std::runtime_error{"Bad result compare at position: " +
                               std::to_string(i)};
    }
  }

  // Print Lo and Hi of matching rows
  // std::cout << "Filter Value" << filter_value << std::endl;
  // for (size_t i = 0; i < num_matches_naive; ++i) {
  //   std::cout << "Lo: " << Low[matching_rows_naive.aligned_data()[i]]
  //             << " Hi: " << High[matching_rows_naive.aligned_data()[i]] <<
  //             std::endl;
  // }

  // Sanity check that the 100 and 0 percent math works out.
  if (input_percentage == 100 && num_matches_specialized != NUM_ROWS) {
    throw std::runtime_error{"Bad result. Did not match all rows."};
  }
  if (input_percentage == 0 && num_matches_specialized != 0) {
    throw std::runtime_error{"Bad result. Did not match 0 rows."};
  }

//   const RowId num_matches = scan_fn(Lo, Hi, filter_value, &matching_rows);
  // std::cout << "matches" << num_matches << std::endl;
  return 0;
}
