#include <bits/stdc++.h>
using namespace std;

int fact(int n){
    if(n <= 1) return 1;
    //n! = n * (n-1)!
    return n*fact(n-1);
}

int power(int x, int n){
    if(n==0) return 1;
    //x^n = x^n-1 * x
    return x * power(x, n-1);
}

void printFrom1toN(int n){
    if(n == 0 ) return; 
    printFrom1toN(n-1);
    cout << n;
}

int main() {
    int n=5;
    cout << fact(n) << endl;

    int x=4, m=3;
    cout << power(x, m) << endl;

    int o=5;
    printFrom1toN(5);
}
