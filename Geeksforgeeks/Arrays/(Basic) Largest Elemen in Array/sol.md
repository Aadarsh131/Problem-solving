## Python

```py 
def largest( arr, n):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    
    return max
    
    #OR using the builtin max fn
    # return max(arr)
```