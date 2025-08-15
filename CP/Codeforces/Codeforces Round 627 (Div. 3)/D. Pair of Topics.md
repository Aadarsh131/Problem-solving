[D. Pair of Topics](https://codeforces.com/problemset/problem/1324/D)

Its just an inversion count problem 
```cpp
#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp>
#include <functional> // for less
#include <iostream>
using namespace __gnu_pbds;
using namespace std;

typedef tree<pair<int,int>, null_type, less<pair<int,int>>, rb_tree_tag,
             tree_order_statistics_node_update>
    PBDS;

int main()
{
    int n;
    cin >> n;
    int a[n],b[n],c[n];

    for(int i=0; i<n; i++){
        cin >> a[i];
    }
    for(int i=0; i<n; i++){
        cin >> b[i];
    }
    for(int i=0; i<n; i++){
        c[i] = a[i] - b[i];
    }

    PBDS p;
    //math behind algo
    //a[i]+a[j] > b[i]+b[j]
    //a[i]-b[i] > -a[i]+b[j]
    //c[i] > -c[j]
    long long inversionCount = 0;
    for(int i=0; i<n; i++){
        
        inversionCount += p.size() - p.order_of_key({-c[i],i});
        p.insert({c[i],i});
    }    
    cout << inversionCount << endl;
}
```