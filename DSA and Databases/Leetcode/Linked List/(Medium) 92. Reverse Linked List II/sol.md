# Approach
General case (when `left`> 2)
> - Keep 1 pointer before the `left` index (named- ***start***) and 1 pointer after the `right` index (named- ***end***)
> - Keep 1 pointer  on index `left` (named- ***p***) and 1 pointer on index `right` (named- ***temp***)
> - We have to reverse the list between node ***p*** and ***temp***

Subproblem (reverse the array)-
> To reverse the linked list, take 2 more pointers ***q*** and ***r***
> > Idea is to traverse the array while keeping 3 pointers ***p***, ***q***, ***r***
> > and on each iteration move each pointer to right (1 step)
> > 1.  ***r*** to ***q***
> > 2. ***q*** to ***p***
> > 3. ***p*** to ***p->next*** 
> >  
> > and while doing so each time make `q->next` point to `r`, i.e, reverse each node to 1 step back 

> Once reversed,
>
>More than half of the task is done, now just left with attaching the nodes to the correct order
>
> The below code comments will follow you up with the approach



# Complexity
- Time complexity: (`Beats 100%` `time: 0ms ` 😻)
    - Best case- **O(1)**
    - Worst case- **O(n)**

- Space complexity: **O(1)**

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
    //no need to check for left and right out of bound, as by default the constraint is set to 1<=left<=right<=n where n is no. of nodes


     ListNode *temp{head}, *start{nullptr}, *p{nullptr}, *q{nullptr}, *r{nullptr};

    //just set start, p and temp
    for (int i = 1; i < right; i++)
    {
        //when left < 3, p and start would not be set(we will handle this case explicitly later)
        temp = temp->next;
        if (i == left - 2)
        {
            start = temp;
        }
        if (i == left - 1)
        {
            p = temp;
        }
    }

    ListNode *end = temp->next;

    //upto now we have-
    //   4      6      7     9    2     1    (left = 3, right = 5)
    // (head) (start) (p)       (temp) (end)

    /* HEAD setting */
    //handling cases explicitly when (left < 3) also setting the new head(if reqd.)
    if (left == 1)
    {
        p = head;
        head = temp;
    //   4      6     7     9      2          1  (IF, left = 1, right = 5)
    //  (p)                   (temp=head)   (end)
    }
    else if (left == 2)
        head->next = temp;
    else
        start->next = temp;

    /* TAIL setting */
    //Reverse the array and also set the reversed list's tail to 'end'
    while (p != end)
    {
        r = q;
        q = p;
        p = p->next;
        if (r == nullptr) //on the first run, set the new tail point to 'end'
            q->next = end;
        else
            q->next = r;
    }

    return head; //return the updated head
  }
};
```