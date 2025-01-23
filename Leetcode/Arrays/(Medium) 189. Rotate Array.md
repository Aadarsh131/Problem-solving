[189. Rotate Array](https://leetcode.com/problems/rotate-array/description/)

## Bruteforce
> Time complexity: $O(n)$  
> Space complexity: $O(n)$
1.  ```cpp
    rotate(vector<int> &arr, int k) {
        vector<int> lastValues;
        int len = arr.size();
        k = k % len;

        for (int i = len - k; i < len; i++) {
          lastValues.push_back(arr[i]);
        };
        for (int i = 0; i < len - k; i++) {
          lastValues.push_back(arr[i]);
        }
        arr = lastValues;
    }
    ```
2.  > NOTE: it is `left shift` not `right shift` (a different problem)
    ```cpp
    #include<bits/stdc++.h>
    using namespace std;

    int arr[] = {1,2,3,4,5,6};

    //shift by k places
    // Time Complexity: O(N+K)
    // Space Complexity: O(K)
    void leftShift(int arr[], int n ,int k){
      if(k<=0){
        return;
      }

      k = k % n;

      vector<int> tempArr;
      for(int i=0; i<k; i++){
        tempArr.emplace_back(arr[i]);
      }

      for(int i=k; i<n; i++){
        arr[i-k] = arr[i];
      }

      for(int i=n-k, j=0; i<n; i++, j++){
        arr[i] = tempArr[j];
      }
    }

    int main(){
      cout << "How many places to be shifted? ";
      int k;
      cin >> k;

      int n = sizeof(arr)/sizeof(arr[0]);

      leftShift(arr, n, k); 

      //print arr
      for(int i=0; i<n; i++){
        cout << arr[i] << " ";
      }
    }
    ```

## Optimal approaches
> Time complexity: $O(n)$  
> Space complexity: 
>  - avg case: $O(n-k)$
>  - worst case: $O(n/2)$
1. This approach is best when `inplace` algo is not reqd. also it only takes upto `O(n/2)` space in worst case 
    ```cpp
    void rotate(vector<int> &nums, int k) {
        int len = nums.size();
        k = k % len;
        vector<int> temp;

        int half = len / 2;
        if (len - k >= half) {
          // then take out (len-k to end) and put it at start
          for (int i = len - k; i < len; i++) {
            temp.push_back(nums[i]);
          }
          nums.erase(nums.begin() + (len - k), nums.end());
          nums.insert(nums.begin(), temp.begin(), temp.end());
          cout << "removed from back inserted at front" << endl;
        }
        // if (len-k < half)
        else {
          // then take out (0 to len-k-1 out) and put it at back
          for (int i = 0; i < len - k; i++) {
            temp.push_back(nums[i]);
          }
          nums.erase(nums.begin(), nums.begin() + len - k);
          nums.insert(nums.end(), temp.begin(), temp.end());
          cout << "removed from front inserted at back" << endl;
        }
    }

    // 1 2 3 4 5
    // 5 1 2 3 4 -> 1 (taking len-1 to end out)
    // 4 5 1 2 3 -> 2
    // 3 4 5 1 2 -> 3 (taking len-3 to end out) -> instead take out (0 to len-3 out)
    // 2 3 4 5 1 -> 4 (taking 0 to len-4 out) and insert at back)
    ```
2. This sol is good when we strictly want `inplace` algo
    ```cpp
    #include<bits/stdc++.h>
    using namespace std;

    int arr[] = {1,2,3,4,5,6,7,8,9};

    void swap(int arr[], int i, int j){
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }

    void reverse(int arr[], int low, int high){
      while(low < high){
        swap(arr,low,high);
        low++;
        high--;
      }
    }

    int main(){
      cout << "How many places to be shifted? ";
      int k;
      cin >> k;

      int size = sizeof(arr)/sizeof(arr[0]);

      reverse(arr,0,k-1); // O(k/2)
      reverse(arr,k,size-1);// O((n-k)/2)
      reverse(arr,0,size-1);// O(n/2)
      //time complexity = O(n)
      //space complexiyt = O(1) (inplace algo)

      //print array
      for(int i=0; i<size; i++){
        cout << arr[i] << " ";
      }
    }
    ```