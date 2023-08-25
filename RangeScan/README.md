This implements a simple range scan mechanism.

Dependencies
clang 15 or above


## Usage

```bash
# For benchmarking
cmake -DCMAKE_BUILD_TYPE=Release .
make -j 10
./bench
./main
```

Multiple implementations
-struct naive_scan (sequential) 
-struct autovec (compiler vectorization)
-128bit_scan_predication (SIMD extraction of all matching, then sequential extraction of matching entries)
-128bit_scan_add (SIMD extraction of all matching, SIMD extraction of matching rows)

## Results
```bash
# ARM M1
-------------------------------------------------------------------------------------------------------------
Benchmark                                                   Time             CPU   Iterations UserCounters...
-------------------------------------------------------------------------------------------------------------
BM_dictionary_scan<naive_scan>/50                         119 us          119 us         5613 PerValue=3.63625ns
BM_dictionary_scan<autovec_scan>/50                      35.8 us         35.8 us        18638 PerValue=1093.61ps
BM_dictionary_scan<vector_128_scan_predication>/50       12.9 us         12.9 us        54260 PerValue=393.175ps
BM_dictionary_scan<vector_256_scan_add>/50               10.7 us         10.7 us        65084 PerValue=326.899ps
```

# Type Description
# One part of the tag array
using KEYCOL = AlignedData<KEYVAL, 64>;

To help the SIMDizer we need to use a column store format
We have to two separate arrays for the Lo and Hi Tags. We keep the Lo and Hi separately to enable SIMD loading of the data. 
Also post matching we need to sequentially extract the matching rows from the data-store since currently there is no indexed accesss to the data-store (atleast not one that I am aware off). 

# Main and usage
