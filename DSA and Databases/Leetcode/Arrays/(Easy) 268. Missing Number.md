[268. Missing Number](https://leetcode.com/problems/missing-number/description/)

## Optimal Sol
1.  > Time Complexity: $O(n)$  
    > Space Complexity: $O(1)$
    ```cpp
    int missingNumber(vector<int>& nums) {
        // using sum of all no. (sum of n natural nos.)
        int n = nums.size();
        int expected_sum;
        if (n % 2 == 0) {
            expected_sum = n / 2 * (n + 1);
        } else {
            expected_sum = n * ((n + 1) / 2);
        }
        int actual_sum = accumulate(nums.begin(), nums.end(), 0);
        return expected_sum - actual_sum;
    }
    ```

2.  >Time Complexity- $O(n)$  
    >Space Complexity- $O(1)$
    ```cpp
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
    ```