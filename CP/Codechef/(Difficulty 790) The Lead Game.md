[The Lead Game](https://www.codechef.com/problems/TLG)

**Cpp**
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int p1s=0, p2s=0; //p1s,p2s represents player 1 and player 2 score resp.
    int maxlead=0,winner=1;
    
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int x=1,a,b;
        while(x--){
            cin >> a;
            p1s +=a;
            
            cin >> b;
            p2s += b;
        }
        if(abs(p1s-p2s) > maxlead){
            maxlead = abs(p1s-p2s);
            winner= (p1s>p2s)?1:2;
        }
    }
    cout << winner << " " << maxlead << endl;
}
```