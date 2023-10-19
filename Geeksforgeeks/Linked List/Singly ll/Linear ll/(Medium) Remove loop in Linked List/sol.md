## Approach- 
**Q.** First we need to find whether the loop exists, and then remove the loop.  

We can sure use the "slow and fast pointer" concept here (Floyd's algorithm) to check if loop exits, but then, to remove the node we have to start the traversing again, this way we are increasing its time complexity.  
Simple way is to use a map/hashtable/dictionary to keep track of the count of traversed nodes, and if count becomes more than 1 for any node, then we will know which node is having the loop and now removing it is pretty straightforward too 

> **Time complexity- O(n)**  
>**Space complexity- O(n)**

<br>

C++
```cpp 
class Solution
{
public:
    // Function to remove a loop in the linked list.
    void removeLoop(Node *head)
    {
        // code here
        // just remove the loop without losing any nodes

        Node *tail = nullptr;
        unordered_map<Node *, int> count;
        while (head)
        {
            count[head]++;
            if (count[head] > 1)
            {
                tail->next = nullptr;
                return;
            }
            tail = head;
            head = head->next;
        }
    }
};
```