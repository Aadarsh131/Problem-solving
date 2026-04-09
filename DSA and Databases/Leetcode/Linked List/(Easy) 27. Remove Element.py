from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        size = len(nums)

        while j < size:
            while j < size and nums[j] == val:
                j += 1

            if j < size:
                if i != j:
                    nums[i] = nums[j]
                i += 1
                j += 1
        return i


s = Solution()
nums = [1,3,2,3,2,4]
val = 2
print(s.removeElement(nums, val))
print(nums)
