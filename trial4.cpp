#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void print(vector<int> vec) {
    for (auto i : vec) {
      cout << i << " ";
    }
  }
  void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int r = m + n - 1;
    int i = m - 1;
    int j = n - 1;

    while (j >= 0) {
      if (i == -1) {
        nums1[r] = nums2[j];
        j--;
        r--;
      } else if (nums1[i] <= nums2[j]) {
        nums1[r] = nums2[j];
        j--;
        r--;
      } else {
        nums1[r] = nums1[i];
        i--;
        r--;
      }
    }
  }
};

int main() {
  vector<int> vec1 = {-1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0};
  // i
  vector<int> vec2 = {-1, -1, 0, 0, 1, 2};
  // j
  Solution a;
  a.merge(vec1, 5, vec2, 6);
  a.print(vec1);
}