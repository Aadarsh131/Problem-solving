## C++
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
    ListNode *start{head};
    ListNode *tail{nullptr};
    while (start != nullptr)
    {
        if (start->val == val)
        {
            // if first node
            if (tail == nullptr)
            {
                tail = start;
                start = start->next;
                head = head->next;
                tail->next = nullptr;
                tail = nullptr;
            }
            else
            {
                tail->next = start->next;
                start->next = nullptr;
                start = tail->next;
            }
        }
        else
        {
            tail = start;
            start = start->next;
        }
    }
    return head;
    }
};
```

## Python3  
(without recursion)
```py
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #without recursion
        if head is None:
            return None
        
        while head and head.val == val:
            head = head.next
        
        i = None
        j = head

        if j is None:
            return None
        
        while j:
            if j.val == val:
                while j and j.val == val:
                    j = j.next
                
                if i.next:
                    i.next = j
            else:
                i = j
                j = j.next

        return head
            
    def printll(self, head: Optional[ListNode]):
            curr = head
            while curr:
                print(curr.val, end='->' if curr.next is not None else '\n')
                curr = curr.next

s = Solution()
head = ListNode(1,ListNode(2,ListNode(1,ListNode(1, ListNode(3, ListNode(4, ListNode(1)))))))
# head = ListNode(1, ListNode(1))
head = s.removeElements(head,1)
s.printll(head)
```

## Python3  
(with recursion)
```py
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #using recursion
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)

        if head.val == val:
            # skip the node
            return head.next
        else:
            return head
```