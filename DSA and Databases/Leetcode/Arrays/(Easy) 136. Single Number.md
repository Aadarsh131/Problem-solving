[136. Single Number](https://leetcode.com/problems/single-number/description/)

```cpp
int singleNumber(vector<int>& nums) {
    //x^x = 0
    //x^x^a = a
    int x=0;
    for(int i: nums){
        x ^= i;
    }
    return x;
}
```