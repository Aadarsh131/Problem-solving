## Python
without sorting
```py
# Optimal solution 
# Time Complexity:`O(n)`
# Space Complexity:`O(1)`

# Find the smallest, second_smallest, largest and second_largest in the arr
arr = [-1,3,3,4,2,6,2,-1,0,9,8,-8.5, 8.2]

min,second_min = float('inf'), float('inf')
max,second_max = float('-inf'), float('-inf')

if len(arr) == 0:
  print('arr is empty')

elif len(arr) == 1:
  min,second_max,max, second_min = arr[0], arr[0],arr[0],arr[0]
  print(min,second_max,max, second_min)

elif len(arr) >= 2:
  for i in arr:
    if i < min:
      second_min = min
      min = i

    if i < second_min and i > min:
      second_min = i
    
    if i > max:
      second_max = max
      max = i
    if i > second_max and i < max:
      second_max = i
  
  print(min,second_min, max, second_max)
```
