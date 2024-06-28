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

```cpp
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
