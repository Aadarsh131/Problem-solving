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
    bool isPalindrome(ListNode* head) {
    ///////by reversing half of the list(efficient way)
            //try it later

    ///////storing the values in a vector, then, finding palindrome
    vector<int> a;
    
    while(head){
        a.emplace_back(head->val);
        head=head->next;
    }

    vector<int>::iterator it = a.begin();
    vector<int>::reverse_iterator r_it = a.rbegin();

    for(int i=0;i<a.size()/2;i++){
        if(*it == *r_it){
            it++;
            r_it++;
        }
        else{
            return 0;
        }
    }
    return 1;




    ///////failing for time limit
       /*
        ListNode* last{head};
        //if list size=1 or empty
        if(head == nullptr || head->next == nullptr)
            return 1;
        //if node size = 2
        if(head->next->next == nullptr)
        {
            if(head->val == head->next->val)
                return 1;
            else
                return 0;
        }
        //move a pointer to 1 node before the last node
        while(last->next->next){//for minimum 3 nodes in list
            last = last->next;
        }
        if(head->val == last->next->val) //checking last and first node's val
        {
            head = head->next;
            last->next = nullptr;
            return isPalindrome(head);
        }
        else{
            return 0;
        }
        */

    }
};
```