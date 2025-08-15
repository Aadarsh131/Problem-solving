[https://www.geeksforgeeks.org/problems/last-index-of-15847/1](https://www.geeksforgeeks.org/problems/last-index-of-15847/1)

**Topics**- Array, Searching
#### Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

#### Note: If '1' is not present, return "-1"
```py
class Solution:
    def lastIndex(self, s: str) -> int:
        for id,item in enumerate(reversed(s),1):
            if item == '1':
                return len(s)-id
        return -1
```    