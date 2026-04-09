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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *temp{list1}, *start{nullptr};

    for (int i = 0; i < b; i++)
    {

        if (i == a - 1)
        { // 1 node before the ath index
            start = temp;
        }
        temp = temp->next;
    }

    start->next = list2;
    start = start->next;

    // traversing with 3 node jumps (approach seems good for big size of linked list)
    while (start)
    {
        if (start->next == nullptr)
        {
            start->next = temp->next;
            temp->next = nullptr;
            return list1;
        }
        else if (start->next->next == nullptr)
        {
            start->next->next = temp->next;
            temp->next = nullptr;
            return list1;
        }
        else if (start->next->next->next == nullptr)
        {
            start->next->next->next = temp->next;
            temp->next = nullptr;
            return list1;
        }
        start = start->next->next->next;
    }
    return nullptr;
       
    }
};
```