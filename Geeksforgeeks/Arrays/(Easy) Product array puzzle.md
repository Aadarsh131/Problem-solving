[Product Array Puzzle](https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1)

**Cpp** (bruteforce)
```cpp
vector<int> res;
int prod = 1;
bool flag = false; //check for 0 in the array
int zero_count=0;

for(int i=0; i<arr.size(); i++){
    if(arr[i] != 0){
        prod *= arr[i];
    }
    else{
        zero_count += 1;
        flag=true; //0 is found
    }
}

for(int i=0; i<arr.size(); i++){
    if(zero_count > 1){
        res.push_back(0);
    }
    else{
        if(flag){
            if(arr[i]==0)
                res.push_back(prod);
            else
                res.push_back(0);
        }
        else
            res.push_back(prod/arr[i]);
    }
}
return res;
```