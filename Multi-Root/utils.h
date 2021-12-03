#include <iostream>
#include "cache.h"
#include <climits>
#include <time.h>
#include <mutex>
#include <atomic>
using namespace std;

std::atomic<uint> insert_flag;
std::mutex mtx2;
std::mutex mtx3;
// int insert_flag=0;

class BTree {
  TreeNode *root;
  int t;

   public:
  BTree(int temp) {
    root = NULL;
    t =temp;
  }

  void traverse() {
    if (root != NULL)
      root->traverse();
  }

  TreeNode *search(int k, RootCache* R1) {
    TreeNode* res1;
    // mtx2.lock();
    TreeNode* ptr= (TreeNode *)R1->Search1(k);
    if(ptr!=NULL){
      // cout<<"not root\n";
      insert_flag=1;
    res1= ptr->search(k, R1);
    // return ptr->search(k, R1);

  }
    else
    {
      insert_flag=0;
    // return (root == NULL) ? NULL : root->search(k, R1);
    res1=(root == NULL) ? NULL : root->search(k, R1);
  }
  // mtx2.unlock();
  return res1;
  }

  void insert(int k);
};

TreeNode::TreeNode(int t1, bool leaf1) {
  t = t1;
  leaf = leaf1;

  keys = new int[2 * t - 1];
  C = new TreeNode *[2 * t];

  n = 0;
}

void TreeNode::traverse() {
  int i;
  for (i = 0; i < n; i++) {
    if (leaf == false){
      C[i]->traverse();
    }

    cout << " " << keys[i];
  }

  if (leaf == false){
    C[i]->traverse();
  }
}


TreeNode *TreeNode::search(int k, RootCache *R1) {

  int i = 0;
  int flg=0;
  TreeNode* res2;
  // mtx3.lock();
  while (i < n && k > keys[i]){
    i++;
  }

  if (keys[i] == k){
    // return this;
    flg=1;
    res2=this;
  }

  if (leaf == true && keys[i]!=k){
    // return NULL;
    flg=1;
    res2=NULL;
  }
    if(insert_flag==0 && i!=n && leaf!=true && keys[i]!=k)
    {
      if(keys[i-1]!=0)
    R1->insert1(keys[i-1], keys[i], (uint64_t)this);
    else //added
    R1->insert1(k, keys[i], (uint64_t)this);//added
    }
  insert_flag=0;
  // mtx3.unlock();
  if(flg==1)
  {
    return res2;
  }
  return C[i]->search(k, R1);
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
