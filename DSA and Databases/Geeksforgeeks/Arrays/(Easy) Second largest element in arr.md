### Python

```py
class Solution:
 def print2largest(self,arr, n):
        max, second_max = float('-inf'), float('-inf')
        for i in arr:
            if i > max:
                 second_max = max
                 max = i

            if i > second_max and i < max:
                 second_max = i
                 
        if second_max == float('-inf'):
            return -1
        else:
            return second_max
```

### C++

1.  ```cpp
    int print2largest(int arr[], int n) {
        int max = arr[0];
        int second_max = -1;
        if (n <= 1){
            return -1;
        }
        for(size_t i=1;i<n;i++){
            if (arr[i]>max){
                second_max = max;
                max = arr[i];
            }
            if (arr[i]>second_max && arr[i]<max){
                second_max = arr[i];
            }
        }
        return second_max;
    }
    ```

2.  ```cpp
    int getSecondLargest(vector<int> &arr) {
        int l=0; //largest
        int sl=1; //second largest

        for(int i=1; i<arr.size(); i++){
            if(arr[i]>arr[l]){
                sl=l;
                l=i;
            }
            if((arr[i]> arr[sl] && arr[i] < arr[l]) || (arr[sl]==arr[l] && arr[i] < sl)){
                sl=i;
            }
        }

        if(arr[l] == arr[sl])
            return -1;
        else
            return arr[sl];
    }
    ```
    - ```cpp
      if((arr[i]> arr[sl] && arr[i] < arr[l]) || (arr[sl]==arr[l] && arr[i] < sl))
      ```
      - we will have three case in the first step when `i=1`
        1. either `arr[i] > arr[l]`, i.e, `l` and `sl` are not in their correct pos, hence we will swap them
        2.  or `arr[i] < arr[l]` , i.e, `l` and `sl` are in their correct pos already, so no need to do anything
        3.  or `arr[i] == arr[l]`, i.e, now `l` and `sl` are the same, which will make a trouble if we donot find any new `l` in the array after it, as then `sl` would remain the largest element until the end, even if it there's an element found to be `< l` (to be a contender of `sl`). Hence to seperate `l` and `sl` we need this condition- `(arr[sl]==arr[l] && arr[i] < sl)`

