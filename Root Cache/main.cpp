

#include <iostream>
#include <thread>
#include <mutex>
#include <fstream>
#include <string>
#include <time.h>
#include "utils.h"
#include <atomic>

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

int main() {
  BTree t(2);
  RootCache R1[4];
  string line;
  ifstream myfile("written.txt");
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

// for(int i = 0; i < 5; i++){
//   cout << "Root Value :"<< t.root->keys[i]<< endl;
// }


// for(int j=0;j<4;j++)
// {
  srand(time(NULL));
int n = 20000;
for(int i = 0; i < 500000; i++){
  int temp = rand()%n +1;
  // cout<<temp<<endl;
  TreeNode* res = t.search(temp, &R1[0]);
  if(res){
    src_count.fetch_add(1);
  }
}

n = 500000;

for(int i = 0; i < 100000; i++){
  int temp = rand()%n +1;
  // cout<<temp<<endl;
  TreeNode* res = t.search(temp, &R1[0]);
  if(res){
    src_count.fetch_add(1);
  }
}
// th[0]=std::thread(search_helper, t, &R1[0], &src_count, 1, 1000000, 0);
  // th[0]=std::thread(search_helper, t, &R1[0], 1, 100000, 0);
  // th[1]=std::thread(search_helper, t, &R1[1], 100001, 200000, 1);
  // th[2]=std::thread(search_helper, t, &R1[2], 900001, 925000, 2);
  // th[3]=std::thread(search_helper, t, &R1[3], 925001, 1000000, 3);

// }



// for(int j=0;j<4;j++)
// {
//   th[j].join();
// }

cout<<endl<<src_count<<"search count"<<endl;

  cout<<R1[0].getHitRate()<<" % Hit Rate"<<endl;
}
