// POTD (15 aug) https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
#include <iostream>

using namespace std;

struct Node
{
  int data;
  Node *next;

  Node(int x)
  {
    data = x;
    next = nullptr;
  }
};

class Solution
{
public:
  // CONSTRAINTS:
  // 0 <= list[i] <= 9
  Node *addOne(Node *head)
  {
    Node *p = nullptr;
    Node *q = head;
    bool flag = 1;
    while (flag)
    {
      while (q != nullptr && q->data != 9)
      {
        p = q;
        q = q->next;
      }
      // if last node is not 9
      if (q == nullptr)
      {
        (p->data)++;
        flag = 0;
        return head;
      }
      while (q != nullptr && q->data == 9)
      {
        q = q->next;
      }
      // if last node is 9
      if (q == nullptr)
      {
        flag = 0;
      }
    }
    // now carry has to be added to prev nodes
    // if head node is 9
    if (p == nullptr)
    {
      Node *newNode = new Node(1);
      newNode->next = head;
      head = newNode;
      Node *temp = head->next;
      while (temp != nullptr)
      {
        temp->data = 0;
        temp = temp->next;
      }
      return head;
    }

    // if p is in some middle of the node
    while (p != nullptr)
    {
      if (p->data != 9)
      {
        (p->data)++;
        p = p->next;
      }
      if (p->data == 9)
      {
        p->data = 0;
        p = p->next;
      }
    }
    return head;
  }
  void print(Node *head)
  {
    Node *temp = head;
    while (temp != nullptr)
    {
      if (temp->next == nullptr)
        cout << temp->data;
      else
        cout << temp->data << " -> ";
      temp = temp->next;
    }
    delete temp;
  }
};

int main()
{
  Solution a;
  Node *head = new Node(9);
  head->next = new Node(9);
  head->next->next = new Node(9);
  head->next->next->next = new Node(9);

  head = a.addOne(head);
  a.print(head);

  delete head->next->next->next;
  delete head->next->next;
  delete head->next;
  delete head;
}