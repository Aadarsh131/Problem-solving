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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *a{l1}, *b{l2};
    int carry = 0;
    int sum = 0;
    while (a || b)
    {
        sum = a->val + b->val + carry;
        if ((sum) / 10)
        { // if found carry
            carry = (sum) / 10;
            a->val = (sum) % 10; // store the one's place value
        }
        else
        {
            a->val = (sum);
            if (carry)
                carry = 0;
        }

        if (a->next == nullptr)
        // l1.len < l2.len then join the node to the l2(b)
        {
            if (carry && b->next == nullptr)
            {
                a->next = new ListNode(carry); // create a new node and store the last carry in it
                a = a->next;
                a->next = nullptr;
                return l1;
            }
            else if (b->next == nullptr) // found no carry
                return l1;
            else
            {
                a->next = b->next;
                a = a->next;
                b->next = nullptr;
                b->val = 0;
            }
        }
        else
            a = a->next;

        if (b->next == nullptr)
        {
            // b->next = nullptr;
            b->val = 0;
        }
        else
            b = b->next;
    }
    return nullptr;
    }
};
```