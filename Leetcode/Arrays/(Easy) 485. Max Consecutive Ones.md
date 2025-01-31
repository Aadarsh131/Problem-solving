[485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/)

> Time Complexity: $O(n)$  
> Space Complexity: $O(1)$

```cpp
int findMaxConsecutiveOnes(vector<int>& nums) {
    int count=0, max_count=0;
    for(auto i: nums){
        if(i == 1){
            count++;
        }
        else if(i != 1){
            max_count = max(count, max_count);
            count=0;
        }
    }
    max_count = max(count, max_count);
    return max_count;
}
```