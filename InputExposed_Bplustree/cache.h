// Searching a key on a B-tree in C++

#include <iostream>
#include <stdint.h>
#include <climits>
#include <mutex>
// #include "utils.h
using namespace std;

std::mutex mtx;

class RootCacheEntry
{

  int start_range_value;
  int end_range_value;
  uint64_t range_address;
  int index_tag;
  long range_size;
  int iterated_levels;


  public:

  int utility_counter;
  uint64_t search_Range(int key, int* rng_sz, uint64_t res, RootCacheEntry searchPoint);
  void insertRange(int start, int end, uint64_t start_address, RootCacheEntry* entrypoint, int number_queries, int iterated_lvs);
  void displayEntry(RootCacheEntry* cursor);
  void flush();
};

uint64_t RootCacheEntry::search_Range(int key, int* rng_sz, uint64_t res, RootCacheEntry searchPoint){
  if(key>=searchPoint.start_range_value && key<=searchPoint.end_range_value)
  {
    if(searchPoint.range_size<*rng_sz)
    {
      // searchPoint.utility_counter++;
      *rng_sz=searchPoint.range_size;
      return searchPoint.range_address;
    }
  }
  return res;
}

void RootCacheEntry::insertRange(int start, int end, uint64_t start_address, RootCacheEntry* entrypoint, int number_queries, int iterated_lvs)
{
  entrypoint->start_range_value=start;
  entrypoint->end_range_value=end;
  entrypoint->range_address=start_address;
  entrypoint->range_size = end - start;
  entrypoint->utility_counter=number_queries;
  entrypoint->iterated_levels=iterated_lvs;



}

void RootCacheEntry::displayEntry(RootCacheEntry* cursor){
    cout<< cursor->start_range_value << ", "<<cursor->end_range_value<< ", "<< cursor->range_address<< ", "<<cursor->range_size<<", "<<cursor->utility_counter<<", "<< cursor->iterated_levels<<endl;
}

class RootCache: public RootCacheEntry
{
  RootCacheEntry* root_cache;
  int size_root_cache;
  long hit_count;
  long number_queries;
  int occupied;

public:
  RootCache(int size)
  {
    cout<<"Constructor\n";
    root_cache = new RootCacheEntry[size];
    size_root_cache=size;
    hit_count=0;
    number_queries=0;
    occupied=0;
  }

  int getSize()
  {
    return size_root_cache;
  }

  uint64_t Search1(int key){
    int rng_sz=INT_MAX;
    uint64_t res=0;
    number_queries++;
    int i = 0;
    int ref = 0;
    for(i=0;i<occupied;i++)
    {
      uint64_t temp = res;
      res = search_Range(key, &rng_sz, res, root_cache[i]);
      if(temp != res){
        ref = i;
      }
    }
    if(res){
      hit_count++;
      root_cache[ref].utility_counter=number_queries;
    }
    // cout<<"\n"<<hit_count<<" Hit Count\n";

    return res;
  }

  void displayRootCache(){
    cout<< "Root Cache Snapshot\n";
    cout<< "No. of Entries Filled: "<< occupied << endl;
    cout<< "Start, "<<"End, "<<"Range Address, "<<"Range Size, "<<"Utility Count"<<"Level Present at\n";

    for(int i = 0; i < occupied; i++)
      displayEntry(&root_cache[i]);

  }

  void insert1(int start, int end, int iter_levels, uint64_t start_address)
  {
    int smallest=0;
    // mtx.lock();
      if(occupied==size_root_cache)
      {
        // cout<<"\nRoot Cache is Full!\n";
        for(int k=0;k<occupied;k++)
        {
          if(root_cache[k].utility_counter<root_cache[smallest].utility_counter)
          {
            smallest=k;
            // insertRange(start, end, start_address, &root_cache[k], number_queries);
            // break;
          }
        }
        insertRange(start, end, start_address, &root_cache[smallest], number_queries, iter_levels);
      }
      else
      {
      insertRange(start, end, start_address, &root_cache[occupied], number_queries, iter_levels);
      occupied++;
      }
      // displayRootCache();
      // cout<<"\nGoing to UNLOCCKKKKKKKK\n";
      // mtx.unlock();
  }

  double getHitRate()
  {
    cout<<hit_count<<" Hit Count\n";
    cout<<number_queries<<" number_queries\n";
    double result=(double)(hit_count*100)/number_queries;

    return result;
  }



};

class TreeNode {
  
  public: 
  int *keys;
  int t;
  TreeNode **C;
  int n;
  bool leaf;

   public:
   
  TreeNode(int temp, bool bool_leaf);

  void insertNonFull(int k);
  void splitChild(int i, TreeNode *y);
  void traverse();

  TreeNode *search(int k, RootCache* R1, int flg, TreeNode* res2, int iter_levels);


  friend class BTree;
};
