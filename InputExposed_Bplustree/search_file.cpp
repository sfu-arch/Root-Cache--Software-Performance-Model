#include <iostream>
#include <fstream>
#include <time.h>
#include "cxxopts.h"

# define DEFAULT_RANGE "1000000"
#define DEFAULT_TYPE "1"
#define DEFAULT_SRANGE "200000"
#define DEFAULT_ERANGE "700000"
#define DEFAULT_RANDOM "30.0"
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
           {"srange", "end range for the intial search before skewed random search in skewed random search",
           cxxopts::value<uint>()->default_value(DEFAULT_SRANGE)},
           {"erange", "start of skewed search for skewed random search",
           cxxopts::value<uint>()->default_value(DEFAULT_ERANGE)},
           {"randomness", "percentage of randomness in search for the 4th search",
           cxxopts::value<double>()->default_value(DEFAULT_RANDOM)},
      });

  auto cl_options = options.parse(argc, argv);
  uint range_max= cl_options["nRange"].as<uint>();
  uint input_typ = cl_options["type"].as<uint>();
  uint start_rng = cl_options["srange"].as<uint>();
    uint end_rng = cl_options["erange"].as<uint>();
    double r = cl_options["randomness"].as<double>();
  
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
  else if (input_typ == 3)
    {
        std::cout << "Skewed Search.\n";
    }
    else if (input_typ == 4)
    {
        std::cout << "Randomised Search.\n";
    }
  int n= range_max;
  int iSecret;
   double range1 = start_rng;
        double range2 = end_rng;
        int i1;
        int i2;
         int k2;
         double rand_per = (r * n / 100);
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
    case 3:
       
        //rand_per has number of random numbers to generate
        
        for (i1 = 1; i1 <= range1; i1++)
        {
            myfile << i1 << " ";
        }

        for (int k1 = range2; k1 <= n; k1++)
        {
            myfile << k1 << " ";
        }
        break;
    case 4:
        //random percentage.
        
        //rand_per has number of random numbers to generate
        
        for (i2 = 1; i2 < (n - rand_per); i2++)
        {
            myfile << i2 << " ";
        }
       
        for (k2 = i2; k2 <= n; k2++)
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
