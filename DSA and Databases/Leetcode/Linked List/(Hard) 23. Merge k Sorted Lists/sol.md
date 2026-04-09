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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
    //     multiset<int> temp;
    // for (int i = 0; i < lists.size(); i++)
    // {
    //     while (lists[i])
    //     {
    //         temp.emplace(lists[i]->val);
    //         lists[i] = lists[i]->next;
    //     }
    // }

    // // ListNode *head = new ListNode(*temp.begin()); // make the first value as head
    // ListNode *start{nullptr}, *head{nullptr};
    // for (auto i = temp.begin(); i != temp.end(); i++)
    // {
    //     if (i == temp.begin())
    //     {
    //         start = new ListNode(*i); // make the first value as head
    //         head = start;
    //     }
    //     else
    //     {
    //         ListNode *temp = new ListNode(*i);
    //         start->next = temp;
    //         start = start->next;
    //     }
    // }
    // temp.clear();

    // return head;

    // using vector
        vector<int> temp;
    for (int i = 0; i < lists.size(); i++)
    {
        while (lists[i])
        {
            temp.emplace_back(lists[i]->val);
            lists[i] = lists[i]->next;
        }
    }

    // ListNode *head = new ListNode(*temp.begin()); // make the first value as head
    sort(temp.begin(),temp.end());
    ListNode *start{nullptr}, *head{nullptr};
    for (auto i = temp.begin(); i != temp.end(); i++)
    {
        if (i == temp.begin())
        {
            start = new ListNode(*i); // make the first value as head
            head = start;
        }
        else
        {
            ListNode *temp = new ListNode(*i);
            start->next = temp;
            start = start->next;
        }
    }
    temp.clear();

    return head;

    }
};
```