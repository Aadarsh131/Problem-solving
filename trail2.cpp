#include <iostream>
#include <numeric>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  int missingNumber(vector<int> &nums) {
    // using xor
    // a^a=0; a^0=a;
    int x = 0, i = 0;
    for (i = 0; i < nums.size(); i++) {
      x ^= i ^ nums[i];
    }
    return x ^ i;
    // eg.
    //[3 0 2]
    //[0 1 2 3]
    // 3 ^ 3 ^ 0 ^ 0 ^ 2 ^ 2 ^ 1 = 1 (XOR is commutative and associative, so the
    // order of operations doesn’t matter)
  }

  void print(vector<int> &arr) {
    for (auto i : arr) {
      cout << i << " ";
    }
  }

  // 1726. tuple with same prroduct
  int tupleSameProduct(vector<int> &nums) {
    unordered_map<int, int> mp;
    int len = nums.size();
    int count = 0;

    for (int i = 0; i < len - 1; i++) {
      for (int j = i + 1; j < len; j++) {
        count += 8 * mp[nums[i] * nums[j]];
        mp[nums[i] * nums[j]]++;
      }
    }
    return count;
  }
};

int main() {
  vector<int> vec = {3, 0, 2};
  // vector<int> vec1 = {2, 4, 5, 1, 10};
  // vector<int> vec1 = {18,1,9,2,6,3};
  // vector<int> vec1 = {2, 3, 4, 6};
  vector<int> vec1 = {1, 36, 2, 18, 3, 12, 4, 9};
  Solution a;
  // cout << a.missingNumber(vec) << endl;
  cout << a.tupleSameProduct(vec1) << endl;
  // a.print(res);
}