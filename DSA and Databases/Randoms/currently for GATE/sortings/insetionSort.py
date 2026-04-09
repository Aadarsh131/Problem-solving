def insertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        insert_idx = i
        for j in range(i-1, -1, -1):
            if A[j] > key:
                A[j+1] = A[j]
                insert_idx = j
            else:
                break
        A[insert_idx] = key

# A = [4,2,6,2,8,4,9,3,6,3]
A = [64, 34, 25, 12, 22, 11, 90, 5]
insertionSort(A)
print(A)

#Time Complexity- Best case: O(n), Worst case: O(n^2)
#Space Complexity- O(1) (inplace algo)
#Stable algo
