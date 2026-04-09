from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if len(nums) == 0:
            return head
        if head is None:
            return None
        
        for num in nums:
            maxi = max(num,maxi) 
        
        while maxi:
            freq = []
    
    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next
        
    
s = Solution()
list = [1,2]
head = ListNode(0, ListNode(2,ListNode(4, ListNode(2,ListNode(2)))))
head = s.modifiedList(list,head)
s.printll(head)
