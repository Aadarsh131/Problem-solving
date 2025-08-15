[Sorted Array Search](https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1)

```cpp
bool searchInSorted(vector<int>& arr, int k) {
    for(int i=0; i<arr.size(); i++){
        if(arr[i] > k){
            return false;
        }else if(k == arr[i]){
            return true;
        }
    }
return false;
}
```