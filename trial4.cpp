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
    int i = 0, j = 0;
    while (i < m && j < n) {
      if (nums1[i] >= nums2[j]) {
        int k = j, count = 0;
        while (k < n && nums1[i] >= nums2[k]) {
          count++;
          k++;
        }

        // pop 'count' items
        for (int a = 0; a < count; a++) {
          nums1.pop_back();
        }

        // insert from (j to k) to i
        nums1.insert(nums1.begin() + i, nums2.begin() + j, nums2.begin() + k);

        // increment i and m by 'count'
        i += count;
        m += count;
        j = k;
      } else
        i++;
    

    // swap the leftover zeroes of nums1
    while (j < n) {
      nums1[i] = nums2[j];
      i++;
      j++;
    }
  }
};

int main() {
  vector<int> vec1 = {-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0};
  // i
  vector<int> vec2 = {-1, -1, 0, 0, 1, 2};
  // j
  // k
  Solution a;
  a.merge(vec1, 5, vec2, 6);
  a.print(vec1);
}