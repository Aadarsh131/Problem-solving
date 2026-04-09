//https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
#include<iostream>

int countDigits(int num) {
        int originalNum = num;
        int count=0,remainder = 0;
        while(num != 0){
        remainder  = num % 10;
        num = num / 10;
        if (originalNum % remainder == 0) {
            count++;
        }
    }
    return count;
}

int main(){
    std::cout << countDigits(123) << std::endl;
}