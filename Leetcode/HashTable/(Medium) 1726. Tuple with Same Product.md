[1726. Tuple with Same Product](https://leetcode.com/problems/tuple-with-same-product/description)

**C++**
```cpp
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
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
```
- DID NOT ACTUALLY KNOW WHY ITS WORKING GO THROUGH IT AGAIN