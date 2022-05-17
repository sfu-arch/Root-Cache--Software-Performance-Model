#include <iostream>
#include "cache.h"
#include <climits>
#include <time.h>
#include <mutex>
#include <atomic>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
int levels = 0;
int arr_levels[120];
FILE *trace_cursor;
// std::atomic<uint> flg;
// flg=0;

std::atomic<uint> insert_flag;
std::mutex mtx2;
std::mutex mtx3;
// int insert_flag=0;

class BTree {
  
  int t;

   public:
   TreeNode *root;
  BTree(int temp) {
    root = NULL;
    t =temp;
  }

  void traverse() {
    if (root != NULL)
      root->traverse();
  }

  void levelTraverse(){
    if(root != NULL)
      root->levelIter(0);
  }

  TreeNode *search(int k, RootCache* R1) {
    TreeNode* res1;
    int iter_done=0;
    int iterLevels=0;
    // mtx2.lock();
    TreeNode* ptr= (TreeNode *)R1->Search1(k, &iterLevels);
    int flg=0;
    TreeNode* res2 = NULL;
    if(ptr!=NULL){
      // cout<<"not root\n";
      insert_flag=1;
      // cout << iterLevels << "\n";
      arr_levels[iterLevels]++;
      res1= ptr->search(k, R1, flg, res2, iterLevels);
      // return ptr->search(k, R1);

  }
    else
    {
      insert_flag=0;
    // return (root == NULL) ? NULL : root->search(k, R1);
    res1=(root == NULL) ? NULL : root->search(k, R1, flg, res2, 1);
  }
  // mtx2.unlock();
  return res1;
  }


  void insert(int k);
  void disp(RootCache* R1);
};

TreeNode::TreeNode(int t1, bool leaf1) {
  t = t1;
  leaf = leaf1;

  keys = new int[2 * t - 1];
  C = new TreeNode *[2 * t];

  n = 0;
  node_util = 0;
}

int level = 0;
int level_utility[12];

void TreeNode::levelIter(int level){
  // cout << "Level "<< level<<endl;
  // cout << "Utility"<<endl;
  // cout<<node_util<<endl;
  // cout<<"occupancy: "<< n << endl;
  level_utility[level]+=node_util;
  node_util = 0;
  for(int i = 0; i <= n; i++){
    if(leaf == false)
      C[i]->levelIter(level+1);
  }
}

void TreeNode::traverse() {
  
  // cout << "Level "<<level<<endl;
  // cout << node_util<< endl;
  int i;
  for (i = 0; i < n; i++) {
    if (leaf == false){
      if(level == 11)
        level = 0;
      level++;
      C[i]->traverse();
    }

    cout << " " << keys[i];
  }
  
  if (leaf == false){
    if(level == 11)
      level = 0;
    level++;
    C[i]->traverse();
  }
}


TreeNode *TreeNode::search(int k, RootCache *R1, int flg, TreeNode* res2, int iter_levels) {

  levels++;
  
  node_util++; //Node utility updated on node search on key.
  int i = 0;
  // flg=0;
  // TreeNode* res2;
  // mtx3.lock();
  while (i < n && k > keys[i]){
    i++;
  }

  if (keys[i] == k){
    // return this;
    flg=1;
    res2=this;
  }
// && keys[i]!=k
  if (leaf == true){
    // return NULL;
    // flg=1;
    if(flg==1)
    {
      flg=0;
      // arr_levels[iter_levels-1]++;
      return res2;
    }
    else{
      // arr_levels[iter_levels-1]++;
      return NULL;
    }
    // res2=NULL;
  }
    if(insert_flag==0 && i!=n && leaf!=true && keys[i]!=k)
    {
      if(keys[i-1]!=0)
        R1->insert1(keys[i-1], keys[i], iter_levels, (uint64_t)this);
      else //added
        R1->insert1(k, keys[i], iter_levels, (uint64_t)this);//added
    }
  insert_flag=0;
  // mtx3.unlock();
  // if(flg==1)
  // {
  //   return res2;
  // }
  iter_levels++;
  return C[i]->search(k, R1, flg, res2, iter_levels);
}

void BTree::disp(RootCache* R1)
{
  R1->displayRootCache();
}

void BTree::insert(int k) {
  if (root == NULL) {
    root = new TreeNode(t, true);
    root->keys[0] = k;
    root->n = 1;
  } else {
    if (root->n == 2 * t - 1) {
      TreeNode *s = new TreeNode(t, false);

      s->C[0] = root;

      s->splitChild(0, root);

      int i = 0;
      if (s->keys[0] < k)
        i++;
      s->C[i]->insertNonFull(k);

      root = s;
    } else
      root->insertNonFull(k);
  }
}

void TreeNode::insertNonFull(int k) {
  int i = n - 1;

  if (leaf == true) {
    while (i >= 0 && keys[i] > k) {
      keys[i + 1] = keys[i];
      i--;
    }

    keys[i + 1] = k;
    n = n + 1;
  } else {
    while (i >= 0 && keys[i] > k)
      i--;

    if (C[i + 1]->n == 2 * t - 1) {
      splitChild(i + 1, C[i + 1]);

      if (keys[i + 1] < k)
        i++;
    }
    C[i + 1]->insertNonFull(k);
  }
}

void TreeNode::splitChild(int i, TreeNode *y) {
  TreeNode *z = new TreeNode(y->t, y->leaf);
  z->n = t - 1;

  for (int j = 0; j < t - 1; j++)
    z->keys[j] = y->keys[j + t];

  if (y->leaf == false) {
    for (int j = 0; j < t; j++)
      z->C[j] = y->C[j + t];
  }

  y->n = t - 1;
  for (int j = n; j >= i + 1; j--)
    C[j + 1] = C[j];

  C[i + 1] = z;

  for (int j = n - 1; j >= i; j--)
    keys[j + 1] = keys[j];

  keys[i] = y->keys[t - 1];
  n = n + 1;
}

