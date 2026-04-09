# binary search (only works in sorted arrays)
# assuming array is sorted in ascending order
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1


def binarySearchRecursive(A,low, high):
    global x
    if low == high:
        return low #or high

    mid = (low+high)//2
    if(A[mid] < x):
        low = mid+1
        return binarySearchRecursive(A,low,high)
    elif(A[mid] > x):
        high = mid-1
        return binarySearchRecursive(A,low,high)
    else:
        return mid

A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# A = [1,3,4,11,14,15]
x = 15
result = binarySearch(A, x)
if result != -1:
  print("Found at index", result, '(iterative approach)')
else:
  print("Not found")

print('Found at index', binarySearchRecursive(A,0,len(A)), '(using recursion)')
    
# Time complexity: T(n) = T(n/2) + c  = O(log n)
# Space complexity: 
#               Iterative search: O(1)
#               Recursive search: O(log n)