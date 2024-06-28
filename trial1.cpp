#include<iostream>
using namespace std;

class Solution {
  public:
    //print second largest number
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
};

int main() {
    int t;
    cout << "how many testcases: ";
    cin >> t;
    while (t--) {
        int n;
        if(n<0){
            cout << "n must be greater than 0" << endl;
            return -1; 
        }
        cout << "Size of arr: ";
        cin >> n;
        if(n<0){
            cout << "n must be greater than 0" << endl;
            return -1; 
        }
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.print2largest(arr, n);
        cout << ans << "\n";
    }
    return 0;
}