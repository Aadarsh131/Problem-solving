#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  // doesnot give distinct 2nd smallest, eg- it outputs 4 for [4,6,4,8]
  int find2ndSmallest(vector<int> &vec) {
    int len = vec.size();
    if (len <= 1) {
      return -1;
    }

    int smallest = 0;
    int smallest_2nd = 1;
    for (int i = 1; i < len; i++) {
      if (vec[i] < vec[smallest]) {
        smallest_2nd = smallest;
        smallest = i;
      } else if (vec[i] < vec[smallest_2nd]) {
        smallest_2nd = i;
      }
    }
    return vec[smallest_2nd];
  }

  // eg. [4,6,4,8] gives 6
  int find2ndSmallestDistinct(vector<int> &vec) {
    int len = vec.size();
    if (len <= 1) {
      return -1;
    }
    int smallest = 0;
    int smallest_distinct2nd = 1;
    for (int i = 1; i < len; i++) {
      if (vec[i] < vec[smallest]) {
        smallest_distinct2nd = smallest;
        smallest = i;
      } else if ((vec[smallest_distinct2nd] == vec[smallest]) &&
                 (vec[i] != vec[smallest])) { // happens only until 1st and 2nd
                                              // lowest are not seperated
        smallest_distinct2nd = i;
      } else if ((vec[i] < vec[smallest_distinct2nd]) &&
                 (vec[i] != vec[smallest])) {
        smallest_distinct2nd = i;
      }
    }
    return vec[smallest_distinct2nd];
  }
};

int main() {
  vector<int> vec1 = {1, 0, 4, 5, 1, 0, 0, 3};
  vector<int> vec2 = {0, 0, 0, 1};

  Solution a;
  assert(a.find2ndSmallest(vec1) == 0);
  assert(a.find2ndSmallest(vec2) == 0);
  assert(a.find2ndSmallestDistinct(vec1) == 1);
  assert(a.find2ndSmallestDistinct(vec2) == 1);
  cout << "All test cases passed!" << endl;
}