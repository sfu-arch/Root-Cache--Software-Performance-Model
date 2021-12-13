#include <iostream>
#include <fstream>
#include <time.h>
#include "cxxopts.h"

# define DEFAULT_RANGE "1000000"
#define DEFAULT_TYPE "1"
using namespace std;

int main(int argc, char *argv[])
{
    cxxopts::Options options("Input Generator",
                           "Generating different kinds of inputs for B-Tree");
  options.add_options(
      "custom",
      {
          {"nRange", "Number of keys to search",
           cxxopts::value<uint>()->default_value(DEFAULT_RANGE)},
          {"type", "Type of search to perform",
           cxxopts::value<uint>()->default_value(DEFAULT_TYPE)},
      });

  auto cl_options = options.parse(argc, argv);
  uint range_max= cl_options["nRange"].as<uint>();
  uint input_typ = cl_options["type"].as<uint>();
  
  std::cout << std::fixed;
  std::cout << "Search from 1 to "<< range_max <<"\n";
  std::cout << "Option Chosen : ";
  if(input_typ==1)
  {
      std::cout << "Serial Search.\n";
  }
  else if(input_typ==2)
  {
      std::cout << "Random Search.\n";
  }
  int n= range_max;
  int iSecret;
  srand(time(NULL));
  ofstream myfile;
 myfile.open("search.txt");
switch(input_typ)
{
case 1:
        for(int i=1;i<=n;i++)
        {
            myfile << i << " ";
        }
break;
    case 2:

    // int n = 1000000;
    for (int i = 1; i <= n; i++)
    {
        iSecret = rand() % n + 1;
        myfile << iSecret << " ";
    }
    
    break;
}
myfile.close();
std::cout << "Done \n";
    return 0;
}