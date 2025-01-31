[Union of 2 Sorted with Duplicates](https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)

```cpp
class Solution {
  public:
    // a,b : the arrays
    // Function to return a list containing the union of the two arrays.
    vector<int> findUnion(vector<int> &a, vector<int> &b) {
        vector<int> res;
        int i = 0, j = 0;
        int len_a = a.size();
        int len_b = b.size();
    
        while (i < len_a && j < len_b) {
          if (a[i] < b[j]) {
            if (res.empty() || res.back() != a[i])
              res.push_back(a[i]);
            i++;
          } else if (b[j] < a[i]) {
            if (res.empty() || res.back() != b[j])
              res.push_back(b[j]);
            j++;
          } else {
            if (res.empty() || res.back() != b[j])
              res.push_back(b[j]);
            i++;
            j++;
          }
        }
        while (j < len_b) {
          if (res.empty() || res.back() != b[j])
            res.push_back(b[j]);
          j++;
        }
        while (i < len_a) {
          if (res.empty() || res.back() != a[i])
          res.push_back(a[i]);
          i++;
        }
        return res;
    }
};
```

1. ## bruteforce
```cpp
#include<bits/stdc++.h>
using namespace std;

int arr1[] = {1,2,2,3,3,4,5};
int arr2[] = {0,1,2,4,4,5,5,6,6};

int main(){
  set<int> temp;

  int n1 = sizeof(arr1)/sizeof(arr1[0]);
  int n2 = sizeof(arr2)/sizeof(arr2[0]);

  //O(n1 logN) (logN is of set insertion complexity and n1 is loop traversal)
  for(int i=0; i<n1; i++){
    temp.insert(arr1[i]);
  }

  //O(n2 logN) 
  for(int i=0; i<n2; i++){
    temp.insert(arr2[i]);
  }

  vector<int> unionn;
  //worst case- O(n1+n2)
  for(auto it : temp){
    unionn.push_back(it);
  }
  
  for(auto it: unionn){
    cout << it;
  }
}
```

2. Using 2 pointers
>   Time complexity: **O(n1+n2)**  
>   Space complexity:   
>   - Worst Case- **O(n1+n2)**
```cpp
#include <bits/stdc++.h>
using namespace std;

int arr1[] = {1, 2, 2, 3, 3, 4, 5};
int arr2[] = {0, 1, 2, 4, 4, 5, 5, 6, 6};

int main()
{
  vector<int> unionn = {999};

  int n1 = sizeof(arr1) / sizeof(arr1[0]);
  int n2 = sizeof(arr2) / sizeof(arr2[0]);

  int i = 0;
  int j = 0;

  while (i < n1 && j < n2)
  {
    while (arr1[i] < arr2[j])
    {
      if (arr1[i] != unionn.back())
      {
        unionn.emplace_back(arr1[i]);
      }
      i++;
    }
    while (arr2[j] < arr1[i])
    {
      if (arr2[j] != unionn.back())
      {
        unionn.emplace_back(arr2[j]);
      }
      j++;
    }
    while (arr1[i] == arr2[j])
    {
      if (arr1[i] != unionn.back())
      {
        unionn.emplace_back(arr1[i]);
      }
      i++;
      j++;
    }
  }

  while (i < n1)
  {
    if (arr1[i] != unionn.back())
    {
      unionn.emplace_back(arr1[i]);
    }
    i++;
  }
  while (j < n2)
  {
    if (arr2[j] != unionn.back())
    {
      unionn.emplace_back(arr2[j]);
    }
    j++;
  }

  //print
  for (int i = 1; i < unionn.size(); i++)
  {
    cout << unionn[i];
  }
}
```