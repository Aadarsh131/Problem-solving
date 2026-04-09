Math intuition- https://youtu.be/dpqpgnTHiLs?si=387r92XFCAimbJ7Z
## C++
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == nullptr || head->next == nullptr )
            return 0;
        ListNode* slow{head},*fast{head};
        while(fast->next && fast->next->next)
        {
            slow=slow->next;
            fast = fast->next->next;
           
            if(slow == fast)
                return 1;
        }
        return 0;
    }
};
```

## Python3
```py
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = fast = head        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
            
        return False

    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next

s = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b; b.next = a
print(s.hasCycle(a))
            
        
```