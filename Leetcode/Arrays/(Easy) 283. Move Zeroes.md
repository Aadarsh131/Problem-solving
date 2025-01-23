[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)

### Better approaches
> Time complexity- $O(n)$  
> Space complexity- $O(1)$ 
1.  ```cpp
    void moveZeroes(vector<int> &nums) {
        int len = nums.size();
        int j = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] != 0) {
                if (i != j) {
                    nums[j] = nums[i];
                }
            j++;
            }
        }
        for (int i = j; i < len; i++) {
            nums[i] = 0;
        }
    }
    ```
2.  ```cpp
    #include<bits/stdc++.h>
    using namespace std;

    int arr[] = {2,0,0,0,0,4,1,6,0,4,0};
    // int arr[] = {1,2,3,4,5};

    void swap(int arr[], int i, int j){
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }

    int main(){
      int n = sizeof(arr)/sizeof(arr[0]);
      
      //search for the first 0
      int i=0;
      while(i<n){
        if(arr[i] == 0) break;
        i++;
      }

      int j = i+1;
      for(j; j<n; j++){
        if(arr[j] ==0){
          continue;
        }
        swap(arr,i,j);
        i++;
      }

      for(int i=0;i<n; i++){
        cout << arr[i] << " ";
      }
    }
    ```

### Bruteforce
> Time complexity- $O(n)$  
> Space complexity- $O(n)$
```cpp
#include<bits/stdc++.h>
using namespace std;

int arr[] = {2,0,5,3,0,4,1,6,0,4,0};
int main(){
  int size = sizeof(arr)/sizeof(arr[0]);
  vector<int> tempArr;

  for(int i=0; i<size; i++){
    if(arr[i] != 0){
      tempArr.emplace_back(arr[i]);
    }
  }
  int i = size-(tempArr.size());
  while(i--){
    tempArr.emplace_back(0);
  }

  //copy tempArr to original arr
  for(int i=0; i<size; i++){
    arr[i] = tempArr[i];
  }
}
```