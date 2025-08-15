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