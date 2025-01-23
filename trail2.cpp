#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
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
  // 1 2 0 0 5
  //   i
  //   j
  void print(vector<int> &arr) {
    for (auto i : arr) {
      cout << i << " ";
    }
  }
};

int main() {
  vector<int> vec = {-8, -3, -3, -2, 0, 1, 2, 2, 6};
  vector<int> vec1 = {-9, -9, 0};
  Solution a;
  vector<int> res = a.findUnion(vec, vec1);
  a.print(res);
}