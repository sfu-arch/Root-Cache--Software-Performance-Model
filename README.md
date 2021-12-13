# Root-Cache--Software-Performance-Model

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

### Bplus Tree Functionality :

Used to create the B+Tree and perform the search functionality with different search workloads.
It is run as follows:

```
g++ -pthread main.cpp

./a.out --degree <num> --cacheSize <cache_size> --inputFile <path_to_file>
```
