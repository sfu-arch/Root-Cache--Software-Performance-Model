g++ search_file.cpp -o search
./search --nRange 10000000 --type 4 --srange 1000000  --erange 9000000 --randomness 80
g++ write_file.cpp -o write 
./write --nRange 10000000 --type 1

g++ main.cpp -o main
./main --nRange 10000000 --degree 5 --cacheSize 1024  --insertFile written.txt --searchFile search.txt > test_sweep.txt