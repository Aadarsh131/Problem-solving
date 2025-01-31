[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

```cpp
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
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
        }

        // swap the leftover zeroes of nums1
        while (j < n) {
            nums1[i] = nums2[j];
            i++;
            j++;
        }
    }
```
Above Sol. Explanation:   
https://leetcode.com/problems/merge-sorted-array/solutions/6321632/omn-time-o1-space-by-aadarshkumar131-2uk0

## Optimal solution
>  Time Complexity:  
>  - Worst Case- $O(m+n)$
>  - Best Case- $O(n)$  
> 
>  Space Complexity: $O(1)$
```cpp
void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int r = m + n - 1;
    int i = m - 1;
    int j = n - 1;

    while (j >= 0) {
      if (i == -1) {
        nums1[r] = nums2[j];
        j--;
        r--;
      } else if (nums1[i] <= nums2[j]) {
        nums1[r] = nums2[j];
        j--;
        r--;
      } else {
        nums1[r] = nums1[i];
        i--;
        r--;
      }
    }
}
```
- `Intuition`: keep the pointers at end of the array, to iterate from back