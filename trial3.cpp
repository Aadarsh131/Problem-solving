#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
      if((m*n) != original.size())
        return {};  
      
      vector<int> temp;
      vector<vector<int>> out;
      int ptr = 0;
      for(int i = 0; i < m; i++){
        for(int j = 0; j< n; j++){
          temp.push_back(original[ptr]); 
          ptr++;
        }
        out.push_back(temp);
        temp.clear();
      }
      return out;
    }

    void print2dArray(vector<vector<int>> out){
      for(const auto items: out){
        for(const int item : items){
          cout << item << " ";
        }
        cout << endl;
      }
    }
};

int main(){
  Solution a;
  vector<int> v = {1,2,3,2,4};
  int m = 2;
  int n = 2;
  a.print2dArray(a.construct2DArray(v,m,n));
}