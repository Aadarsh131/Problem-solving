## Python
```py
class Solution:
	def print2largest(self,arr, n):
        max, second_max = float('-inf'), float('-inf')
        for i in arr:
            if i > max:
                 second_max = max
                 max = i

            if i > second_max and i < max:
                 second_max = i
                 
        if second_max == float('-inf'):
            return -1
        else:
            return second_max
```
