def selectionSort(A):
    for i in range(len(A)):
        min = A[i]
        min_loc = i
        for k in range(i+1,len(A)):
            if A[k] < min: 
                min = A[k]
                min_loc = k
        A[i],A[min_loc]=A[min_loc],A[i]
    
# skipped keeping track of minimum explicitly, just keeping track of min_location
def selectionSort2(A):
    for i in range(len(A)):
        min_loc = i
        for k in range(i+1,len(A)):
            if A[k] < A[min_loc]: 
                min_loc = k
        A[i],A[min_loc]=A[min_loc],A[i]


A = [7,1,4,2,5,2,6,1,0,3]
# selectionSort(A)
selectionSort2(A)
print(A)

# Time Complexity  - O(n^2) -best and worst case both
# Space Complexity - O(1)
# Inplace sort
# Unstable sort (eg. take A = [3,3,1])