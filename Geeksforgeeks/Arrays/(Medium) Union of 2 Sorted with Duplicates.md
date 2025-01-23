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
    //[4 5 9 10]   [1 2 9]  
    //       i            j
    //[1 2 4 5 9 10]
    
    //[1 2 3 4 5]  [1 2 3]
    //         i          j
    //[1 2 3 4 5]
};
```