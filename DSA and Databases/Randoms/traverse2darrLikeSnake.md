**Question**: traverse the 2d array like snake starting from top to bottom, snake cannot move in the same column again, if it has travelled one column it moves to its immediate right column and travel from bottom to top to travel all the elements and so on.

If 2d array is this-  
 {1, 2, 3, 4}  
 {5, 6, 7, 8}  
 {9, 10, 11, 12}  
 {13,14, 15, 16}

then, output should be: 1,5,9,13,14,10,6,2,3,7,11,15,16,12,8,4

```cpp
#include<iostream>
#include<vector>
using namespace std;

// eg. If 2d array is this-
// {1, 2,  3,   4}
// {5, 6,  7,   8}
// {9, 10, 11, 12}
// {13,14, 15, 16}
//
// then, output should be: 1,5,9,13,14,10,6,2,3,7,11,15,16,12,8,4

int main(){
    int n;
    cin >> n;
    int** _2darr = new int*[n];
    for(int i=0; i<n; i++){
        _2darr[i] = new int[n];
        for(int j=0; j<n; j++){
            cin >> _2darr[i][j];
        }
    }

    int j=0;
    while(j<n){
        if(j%2==0){
            for(int i=0; i< n; i++){
                cout << _2darr[i][j] << " ";
            }
        }
        else{
            for(int i=n-1; i>=0; i--){
                cout << _2darr[i][j] << " ";
            }
        }
        j++;
    }
    
    //deallocating memory
    for(int i=0; i<n; i++){
        delete _2darr[i];
    }
    delete[] _2darr;
}
```
