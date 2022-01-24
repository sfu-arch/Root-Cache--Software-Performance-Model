g++ search_file.cpp -o search
./search --nRange 1000000 --type 1 
g++ write_file.cpp -o write 
./write --nRange 1000000 --type 1

g++ main.cpp -o main
./main --nRange 1000000 --degree 5 --cacheSize 1024  --insertFile written.txt --searchFile search.txt