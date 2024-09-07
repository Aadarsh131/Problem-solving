from typing import List
class Solution:
    def construct2dArray(self, original: List[int], m:int, n:int) -> List[List[int]]:
      if (m*n) != len(original):
        return []
      else:
        # this initialization will not work, this type of initialization does not create independent lists for each row. Instead, it creates a list of references to the same list, which causes the mutation of one row to affect all rows.
        # out = [[0]*n]*m

         # Initialize 2D array with independent rows
        out = [[0] * n for _ in range(m)]
        ptr = 0
        for i in range(m):
          for j in range(n):
            out[i][j] = original[ptr]
            ptr += 1
        return out 
if __name__ == "__main__":
    a = Solution()
    _1dArray = [3,4,6,2,5,7]
    m = 3
    n = 2
    print(a.construct2dArray(_1dArray, m, n))

# def reverse_signedInt(n:int) -> int:
#   #setting the range as per question constraint (32 signed bit integer)
#   INT_MAX = 2**32 - 1
#   INT_MIN = -2**32

#   sign = -1 if n < 0 else 1
#   n = abs(n)


# #   while(n>0):
# #     last = n % 10
# #     n //= 10

# reverse_signedInt(-24422)

