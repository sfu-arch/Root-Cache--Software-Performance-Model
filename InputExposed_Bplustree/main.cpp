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

#define DEFAULT_RANGE "1000000"
#define DEFAULT_DEGREE "2"
#define DEFAULT_THREAD_COUNT "4"

using namespace std;

std::mutex mtx1;
std::atomic<int> src_count;
std::atomic<int>total_count;
//
void search_helper(BTree t, RootCache* R1, int start_ind, int end_ind, int thread_id)
{
  int insert_flag=0;
  TreeNode* resres;
  // cout<<endl<<src_count<<"search count"<<endl;
  for(int j=start_ind;j<=end_ind;j++)
  {
    insert_flag=0;
    // mtx1.lock();
    resres=t.search(j,R1);
    if(resres)
    {
      src_count.fetch_add(1);
    }
    total_count.fetch_add(1);
    // mtx1.unlock();
    if(total_count%1000000 == 0){
      // cout<<"Search No. "<<j<<endl;
      // cout<<"--------------------------------------------------------------------"<<endl;
      // cout<<endl;
      // t.disp(R1);
      // cout<<"--------------------------------------------------------------------"<<endl;
      // cout<<endl;
      R1->displayCacheDist();
    }
  }
  
  // mtx1.lock();
  // cout << "Thread ID: "<<src_count<<endl;
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
          {"nRange", "N",
           cxxopts::value<uint>()->default_value(DEFAULT_DEGREE)},
          {"degree", "Degree of B-Tree",
           cxxopts::value<uint>()->default_value(DEFAULT_DEGREE)},
           {"cacheSize", "Cache Size",
           cxxopts::value<uint>()->default_value(DEFAULT_THREAD_COUNT)},
          {"insertFile", "Input insert elements",
           cxxopts::value<std::string>()->default_value(
               "written.txt")},
          {"searchFile", "Input search elements",
           cxxopts::value<std::string>()->default_value(
               "search.txt")},
      });

  auto cl_options = options.parse(argc, argv);
  uint range = cl_options["nRange"].as<uint>();
  uint deg = cl_options["degree"].as<uint>();
  uint cache_size = cl_options["cacheSize"].as<uint>();
  std::string insert_file_path = cl_options["insertFile"].as<std::string>();
  std::string search_file_path = cl_options["searchFile"].as<std::string>();
  std::cout << std::fixed;
  std::cout << "N : " << range << "\n";
  std::cout << "BTree Degree : " << deg << "\n";
  std::cout << "Cache Size : " << cache_size << "\n";
  std::cout << "Insert File Name : " << insert_file_path << "\n";
  std::cout << "Search File Name : " << search_file_path << "\n";

  BTree t(deg);
RootCache R1(cache_size);
  string line;
  ifstream myfile(insert_file_path);
  int numb;
  for(int i = 0; i < range; i++){
    if (myfile.is_open())
    {
      while (getline(myfile, line, ' '))
      {
        numb = std::stoi(line);
        t.insert(numb);
      }
      myfile.close();
    }
      // t.insert(i);
  }



src_count = 0;
total_count = 0;
// std::thread th[4];

//division of the root amongst the threads 

//lets see what the root looks like 

// for(int i = 0; i <3; i++){
//   cout << "Root Value :"<< t.root->keys[i]<< endl;
// }


// for(int j=0;j<4;j++)
// {
//   srand(time(NULL));
// int n = 1000000;
// for(int i = 0; i < 1000000; i++){
//   int temp = rand()%n +1;
//   // cout<<temp<<endl;
//   TreeNode* res = t.search(temp, &R1);
//   if(res){
//     src_count.fetch_add(1);
//   }
// }
// for(int i=1;i<=1000000;i++)
// {
// t.search(i, &R1);
// }
// n = 500000;

// for(int i = 0; i < 100000; i++){
//   int temp = rand()%n +20000;
//   // cout<<temp<<endl;
//   TreeNode* res = t.search(temp, &R1[0]);
//   if(res){
//     src_count.fetch_add(1);
//   }
// }
//

// }
// cout<<endl<<src_count<<"search count"<<endl;
string line1;
ifstream myfile1(search_file_path);
int numb1;
for(int i=0;i<range;i++)
{
  if (myfile1.is_open())
    {
      while (getline(myfile1, line1, ' '))
      {
        numb1 = std::stoi(line1);
        search_helper(t, &R1, numb1, numb1, 0);
      }
      myfile1.close();
    }
}
// search_helper(t, &R1, 1000000, 1000000, 0);



// for(int j=0;j<1;j++)
// {
//   th[j].join();
// }

// t.levelTraverse();

cout<<endl<<src_count<<"search count"<<endl;

  cout<<R1.getHitRate()<<" % Hit Rate"<<endl;
cout<<levels<<" Levels iterated over"<<endl;
cout<<"Level, Frequency"<<endl;
for(int i = 0; i < 11; i++){
  cout << i+1<<", "<<arr_levels[i]<<endl;
}
}
