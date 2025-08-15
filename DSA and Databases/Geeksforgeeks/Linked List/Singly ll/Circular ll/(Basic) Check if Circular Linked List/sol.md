C++
```cpp
/* Should return true if linked list is circular (empty list is circular), else false */
bool isCircular(Node *head)
{
   Node* start{head};
   
   if(head == nullptr){
        return 1;
   }
   else
   {
       while(start != nullptr)
       {
            start = start->next;  
           if(start == head)
                return 1;
       }
       return 0;
   }
}
```