#include<iostream>

//nCr = n-1Cr-1 + n-1Cr (Pascals' Rule)
int nCr(int n, int r){
    if( r==0 || r==n) return 1;
    if(r==1) return n;
    if( r>n) return 0;
    return nCr(n-1, r-1) + nCr(n-1, r);
}

int main(){
    std::cout<< nCr(5, 2) << std::endl;
}