> https://leetcode.com/problems/count-numbers-with-unique-digits/description/

#### <u>Approach/Intuition:</u>
 > *Combinatorics + dynamic programming problem*
- For n=0, we have only 1 number (0) with unique digits
- For n=1, we have 10 from 0-9 unique digits
- For n=2, unique 2 digit number can be choosen in 9*9 ways, then remaining 1 digit number can be added onto it
  - `f(2) = 9*9 + f(1)`
- so, in general `f(n) = 9*9*8*...*(10-n+1) + f(n-1)`
  
#### <u>Solution:</u>
- [c++](#c)

#### C++
```cpp
int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1;
    if (n == 1) return 10;
    
    int out=1;
    for(int i=10-n+1; i<=9; i++){
        out *= i;
    }
    return out * 9 + countNumbersWithUniqueDigits(n-1);
}
```
