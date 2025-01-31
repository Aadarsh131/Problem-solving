#include <iostream>
#include <numeric>
#include <set>
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
    return x^i;
    //eg.
    //[3 0 2]
    //[0 1 2 3]
    //3 ^ 3 ^ 0 ^ 0 ^ 2 ^ 2 ^ 1 = 1 (XOR is commutative and associative, so the order of operations doesn’t matter)
  }

  void print(vector<int> &arr) {
    for (auto i : arr) {
      cout << i << " ";
    }
  }
};

int main() {
  vector<int> vec = {3, 0, 2};
  Solution a;
  cout << a.missingNumber(vec) << endl;
  // a.print(res);
}