# O(n^2) in best case
def bubbleSort(A):
    total_comparisons = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            total_comparisons += 1
            if A[j] > A[j+1]: 
                A[j], A[j+1] = A[j+1], A[j]
    print(total_comparisons)

# O(n) in best case
def bubbleSortOptimized(A):
    total_comparisons = 0
    for i in range(len(A)):
        flag = 0
        for j in range(len(A)-i-1):
            total_comparisons += 1
            if A[j] > A[j+1]: 
                A[j], A[j+1] = A[j+1], A[j]
                flag += 1
        if flag == 0: 
            print('priting early')
            print(total_comparisons)
            return
    print(total_comparisons)

A = [4,3,5,2,-2,1]
# B = [1,2,3,4,5,6,7,8,9]
bubbleSort(A)
print(A)
print()

bubbleSortOptimized(A)
print(A)

# Time Complexity (with bubbleSort() algo)- 
#           Best case:  O(n^2)    
#           Worst Case: O(n^2)
#
# Time Complexity (with bubbleSortOptimized() algo)- 
#           Best case:  O(n)    
#           Worst Case: O(n^2)
#
# Space Complexity- O(1)
# Inplace algorithm
# Stable algo