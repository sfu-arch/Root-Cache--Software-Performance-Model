# Index Cache: Architectural Model

The Model is located in `InputExposed_Bplustree`. 
The model is split into the Input Generator and the Bplus Tree Functionality.

### Input Generator : 

Used to generate different types of input workloads.
It is run as follows:

```
g++ write_file.cpp

./a.out --nRange <n> --type <1/2>
```

Type 1: Serial Input 1-n are generated and written to the text file.

Type 2: Random numbers between 1-n are generated and written to the text file.

### Search Script : 

Used to search B-Tree by generating different traffic to search.
It is run as follows:

```
g++ search_file.cpp

./a.out --nRange <n> --type <1/2/3/4> --srange <end_first_part> --erange <start_second_part> --randomness <percentage_of_randomness>
```

Type 1: Serial Input 1-n are generated and written to the text file.

Type 2: Random numbers between 1-n are generated and written to the text file.

Type 3: Utilises the `srange` and `erange` parameters, to set the end_range of search for the first part of the search. The skewed search starts from erange.

Type 4: Utilises the `randomness` to set the percentage of random numbers to search out of the total number of keys to search, `srange` and `erange` parameters, to set the end_range of search for the first part of the search parameter. Sequential Search till srange then random till 30% of n, then start sequential from erange.

These then aid in searching the B-Tree.

### Bplus Tree Functionality :

Used to create the B+Tree and perform the search functionality with different search workloads.
It is run as follows:

```
g++ main.cpp

./a.out --nRange <N> --degree <num_degree> --cacheSize <cache_entries> --insertFile <path_to_file> --searchFile <path_to_file>    
```
