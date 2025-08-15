[1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/description/)

**Cpp**

> **Approach**: Sliding window with hashmap to track characters and their counts
```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> nums {5,2,1,2,5,2,1,2,5};
    int len = nums.size();

    int i=0,j=0;
    int sum=0;
    map<int, int> charCount;
    int score = 0;
    while(j < len){
        charCount[nums[j]]++;
        if(charCount[nums[j]] > 1){
            score = max(score, sum);
            while(nums[i] != nums[j]){
                charCount[nums[i]]--;
                sum -= nums[i];
                i++;
            }
            charCount[nums[i]]--;
            sum -= nums[i];
            i++;
        }
        sum+=nums[j];
        j++;
    }
    score = max(score, sum);
    cout << score << endl;
}
``