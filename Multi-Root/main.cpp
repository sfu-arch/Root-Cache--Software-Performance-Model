

#include <iostream>
#include <thread>
#include <mutex>
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
  for(int i = 1; i <= 1000000; i++){
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

// th[0]=std::thread(search_helper, t, &R1[0], &src_count, 1, 1000000, 0);
  th[0]=std::thread(search_helper, t, &R1[0], 1, 250000, 0);
  th[1]=std::thread(search_helper, t, &R1[1], 250001, 500000, 1);
  th[2]=std::thread(search_helper, t, &R1[2], 500001, 750000, 2);
  th[3]=std::thread(search_helper, t, &R1[3], 750001, 1000000, 3);

// }



for(int j=0;j<4;j++)
{
  th[j].join();
}

cout<<endl<<src_count<<"search count"<<endl;

  cout<<R1[0].getHitRate()<<" % Hit Rate"<<endl;
}
