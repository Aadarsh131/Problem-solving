#https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        prev = None
        curr = head
        next = curr.next

        while next:
            curr.next = prev

            prev = curr
            curr = next
            next = next.next

        curr.next = prev
        return curr

    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next

s = Solution()
# head = None
head = ListNode(1,ListNode(2))
head = s.reverseList(head)
s.printll(head)