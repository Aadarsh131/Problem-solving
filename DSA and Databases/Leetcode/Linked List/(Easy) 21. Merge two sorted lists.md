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

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        if (list1 == nullptr && list2 == nullptr)
            return nullptr;
        if (list2 == nullptr)
            return list1;
        if (list1 == nullptr)
            return list2;

        ListNode *start, *p;
        if (list1->val < list2->val)
        {
            p = start = list1;
            list1 = list1->next;
            p->next = nullptr;
        }
        else
        {
            p = start = list2;
            list2 = list2->next;
            p->next = nullptr;
        }

        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                p->next = list1;
                list1 = list1->next;
                p = p->next;
                p->next = nullptr;
            }
            else
            {
                p->next = list2;
                list2 = list2->next;
                p = p->next;
                p->next = nullptr;
            }
        }
        if (list1 == nullptr)
            p->next = list2;
        else
            p->next = list1;

        return start;
    }
};
```
<br>

## Python3 
```py
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2

        if i is None:
            return j        
        if j is None:
            return i
        
        head = None
        if i.val <= j.val:
            head = i
        else:
            head = j
        
        inext = jnext = None 
        while i and j:
            if i and i.val <= j.val:
                while i and i.val <= j.val:
                    if i.next is not None and i.next.val <= j.val:
                        i = i.next
                    else:
                        break

                inext = i.next
                i.next = j
                i = inext

            else:
                while j and j.val < i.val:
                    if j.next is not None and j.next.val < i.val:
                        j = j.next
                    else:
                        break

                jnext = j.next
                j.next = i
                j = jnext
        return head

    def printll(self, head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, end='->' if curr.next is not None else '\n')
            curr = curr.next
s = Solution()
l1 = ListNode(1, ListNode(1,ListNode(2,ListNode(5,ListNode(6)))))
l2 = ListNode(-1, ListNode(0, ListNode(3, ListNode(5))))
# l1 = None
# l2 = ListNode(1) 
merged = s.mergeTwoLists(l1,l2)
s.printll(merged)

```

## Go

```go
package main

import "fmt"

func main(){
    fmt.Println("Solution coming soon!")
}
```