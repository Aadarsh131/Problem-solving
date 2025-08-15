[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

**Cpp**  
> **Approach**: Sliding window with hashmap to track characters and their counts
```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){
    string s = "dvdf";
    int len = s.length();

    int i=0,j=0;
    map<char, int> charCount;
    int longestSubstrlen = 0;
    while(j < len){
        charCount[s[j]]++;
        if(charCount[s[j]] > 1){
            //first record the longest substring length
            longestSubstrlen = max(longestSubstrlen, j - i);

            while(s[i] != s[j]){
                charCount[s[i]]--;
                i++;
            }
            charCount[s[i]]--;
            i++;
        }
        j++;
    }
    longestSubstrlen = max(longestSubstrlen, j - i);
    cout << longestSubstrlen << endl;
}
```