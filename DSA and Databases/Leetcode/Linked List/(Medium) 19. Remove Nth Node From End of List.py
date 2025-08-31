from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return

        i = head
        prev = j = i

        #assumed n is never out of range as per que
        while n>1:
            i = i.next
            n -= 1
        
        while i.next:
            i = i.next
            if i.next is None:
                j = j.next
            else:
                j = j.next
                prev = j

        if j == head:
            head = j.next
            return head
        prev.next = prev.next.next
        return head
        
    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next
            
s = Solution()
ll = ListNode(1,ListNode(2,ListNode(3)))
ll = s.removeNthFromEnd(ll,3)
s.printll(ll)