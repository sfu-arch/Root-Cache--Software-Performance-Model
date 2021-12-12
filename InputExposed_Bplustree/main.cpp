//pull out degree, number of threads, file as a parameter

#include <iostream>
#include <thread>
#include <mutex>
#include <fstream>
#include <string>
#include <time.h>
#include "utils.h"
#include <atomic>
#include <iomanip>
#include <stdlib.h>
#include "cxxopts.h"

#define DEFAULT_DEGREE "2"
#define DEFAULT_THREAD_COUNT "4"

using namespace std;

std::mutex mtx1;
std::atomic<int> src_count;
//
void search_helper(BTree t, RootCache* R1, int start_ind, int end_ind, int thread_id)
{
  int insert_flag=0;
  TreeNode* resres;
  for(int j=start_ind;j<=end_ind;j++)
  {
    insert_flag=0;
    // mtx1.lock();
    resres=t.search(j,R1);
    if(resres)
    {
      src_count.fetch_add(1);
    }
    // mtx1.unlock();
  }
  // mtx1.lock();
  cout << "Thread ID: "<<src_count<<endl;
  // R1->displayRootCache();
  // mtx1.unlock();
}

int main(int argc, char *argv[]) {

// cxxopts::Options options("pi_calculation",
//                            "Calculate pi using serial and parallel execution");
//   options.add_options(
//       "custom",
//       {
//           {"nPoints", "Number of points",
//            cxxopts::value<uint>()->default_value(DEFAULT_NUMBER_OF_POINTS)},
//           {"nWorkers", "Number of workers",
//            cxxopts::value<uint>()->default_value(DEFAULT_NUMBER_OF_WORKERS)},
//       });

//   auto cl_options = options.parse(argc, argv);
//   uint n_points = cl_options["nPoints"].as<uint>();
//   uint n_workers = cl_options["nWorkers"].as<uint>();
//   std::cout << std::fixed;
//   std::cout << "Number of points : " << n_points << "\n";
//   std::cout << "Number of workers : " << n_workers << "\n";


cxxopts::Options options(
      "main",
      "Root Cache Software Performance Model");
  options.add_options(
      "custom",
      {
          {"degree", "Degree of B-Tree",
           cxxopts::value<uint>()->default_value(DEFAULT_DEGREE)},
           {"cacheSize", "Cache Size",
           cxxopts::value<uint>()->default_value(DEFAULT_THREAD_COUNT)},
          {"inputFile", "Input insert elements",
           cxxopts::value<std::string>()->default_value(
               "writ.txt")},
      });

  auto cl_options = options.parse(argc, argv);
  uint deg = cl_options["degree"].as<uint>();
  uint cache_size = cl_options["cacheSize"].as<uint>();
  std::string input_file_path = cl_options["inputFile"].as<std::string>();
  std::cout << std::fixed;
  std::cout << "BTree Degree : " << deg << "\n";
  std::cout << "Number of Threads : " << cache_size << "\n";
  std::cout << "Input File Name : " << input_file_path << "\n";

  BTree t(deg);
  // RootCache(1024);
  RootCache R1(cache_size);
  string line;
  ifstream myfile(input_file_path);
  int numb;
  for(int i = 1; i <= 1000000; i++){
    // if (myfile.is_open())
    // {
    //   while (getline(myfile, line, ' '))
    //   {
    //     numb = std::stoi(line);
    //     t.insert(numb);
    //   }
    //   myfile.close();
    // }
      t.insert(i);
  }



src_count = 0;

std::thread th[4];

//division of the root amongst the threads 

//lets see what the root looks like 

// for(int i = 0; i <3; i++){
//   cout << "Root Value :"<< t.root->keys[i]<< endl;
// }


// for(int j=0;j<4;j++)
// {
  srand(time(NULL));
int n = 1000000;
for(int i = 0; i < 1000000; i++){
  int temp = rand()%n +1;
  // cout<<temp<<endl;
  TreeNode* res = t.search(temp, &R1);
  if(res){
    src_count.fetch_add(1);
  }
}

// n = 500000;

// for(int i = 0; i < 100000; i++){
//   int temp = rand()%n +20000;
//   // cout<<temp<<endl;
//   TreeNode* res = t.search(temp, &R1[0]);
//   if(res){
//     src_count.fetch_add(1);
//   }
// }
// th[0]=std::thread(search_helper, t, &R1[0], &src_count, 1, 1000000, 0);
  // th[0]=std::thread(search_helper, t, &R1[0], 1, 100000, 0);
  // th[1]=std::thread(search_helper, t, &R1[1], 100001, 200000, 1);
  // th[2]=std::thread(search_helper, t, &R1[2], 900001, 925000, 2);
  // th[3]=std::thread(search_helper, t, &R1[3], 925001, 1000000, 3);
  // th[0]=std::thread(search_helper, t, &R1, 1, 1000000, 0);
  // th[1]=std::thread(search_helper, t, &R1[1], 250001, 500000, 1);
  // th[2]=std::thread(search_helper, t, &R1[2], 500001, 750000, 2);
  // th[3]=std::thread(search_helper, t, &R1[3], 750001, 1000000, 3);

// }



// for(int j=0;j<1;j++)
// {
//   th[j].join();
// }

cout<<endl<<src_count<<"search count"<<endl;

  cout<<R1.getHitRate()<<" % Hit Rate"<<endl;
cout<<levels<<" Levels iterated over"<<endl;
}
