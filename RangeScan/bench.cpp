#include "range_scan.hpp"

using vector_128_scan_add = vector_scan_add<16, uint32_t>;
// using uint8_t as RowOffsetT didn't give a measurable performance boost on
// icelake, but it decreases GCC performance
using vector_256_scan_add = vector_scan_add<32, uint32_t>;


#define BM_ARGS Unit(benchmark::kMicrosecond)->Arg(50)

BENCHMARK(BM_dictionary_scan<naive_scan>)->BM_ARGS;
BENCHMARK(BM_dictionary_scan<autovec_scan>)->BM_ARGS;

// BENCHMARK(BM_dictionary_scan<vector_128_scan_shuffle>)->BM_ARGS;
BENCHMARK(BM_dictionary_scan<vector_128_scan_predication>)->BM_ARGS;
BENCHMARK(BM_dictionary_scan<vector_256_scan_add>)->BM_ARGS;

BENCHMARK_MAIN();
