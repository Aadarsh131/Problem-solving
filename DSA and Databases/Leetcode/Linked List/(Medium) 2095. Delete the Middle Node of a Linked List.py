# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
       
        if fast.next is None:
            head = head.next
            return head

        if fast.next.next is None:
            head.next = None
            return head

        while fast.next and fast.next.next:
            fast = fast.next.next
            if fast.next is None:
                slow.next = slow.next.next
                return head

            if fast.next.next is None:
                slow = slow.next
                slow.next = slow.next.next
                return head
            
            slow = slow.next

    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next

s = Solution()
# ll = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
ll = ListNode(1, ListNode(3))
ll = s.deleteMiddle(ll)
s.printll(ll)
            
        