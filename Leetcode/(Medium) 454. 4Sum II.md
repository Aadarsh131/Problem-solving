> https://leetcode.com/problems/4sum-ii/description/
### 1. BruteForce- O(n^4)
```cpp
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int count = 0;
        for(int i: nums1){
            for(int j: nums2){
                for(int k: nums3){
                   for(int l: nums4){
                      if(i+j+k+l == 0)
                        count++;
                   }
                }
            }
        }
        return count;
    }
};
```

#### 2. Optimal Sol- O(n^2)
```cpp
int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int count = 0;
        unordered_map<int,int> mp;

        //O(n^2)
        for(int i: nums1)
            for(int j: nums2)
                mp[i+j]++;

        //O(n^2)
        for(int k: nums3)
            for(int l: nums4)
                count += mp[-(k+l)];

        return count;
    }
```


