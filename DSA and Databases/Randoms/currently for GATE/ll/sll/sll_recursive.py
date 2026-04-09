# Recursive insertion and traversal in a singly linked list 
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_end(head, data):
    if head is None:
        return Node(data)

    head.next = insert_end(head.next, data)
    return head


def traverse(head):
    if head is None:
        return

    print(head.data, end="->" if head.next != None else "\n")
    traverse(head.next)

def traverseReverse(head):
    if head is None:
        return
    
    traverseReverse(head.next)
    print(head.data, end=' ')

def reverseSll(head):
    if head is None or head.next is None:
        return head
    
    head.next.next = reverseSll(head.next)#head
    return head

#                           f(1)
#                           /   \
#           1.next.next = f(2)   1
#                         /  \
#         2.next.next = f(3)  1 
#                       /   \
#     3.next.next = f(none)  2

def sum1(head, total=0):
    if head is None:
        return total
    total += head.data
    return sum1(head.next, total)

#OR
def sum2(head):
    if head is None:
        return 0
    return head.data + sum2(head.next)

def length(head):
    if head is None:
        return 0
    return 1+length(head.next)

if __name__ == "__main__":
    # Insert nodes with data 1, 2, 3, 4, 5
    head = None
    head = insert_end(head, 1)
    head = insert_end(head, 2)
    head = insert_end(head, 3)
    # head = insert_end(head, 4)
    # head = insert_end(head, 5)

    traverse(head)
    traverseReverse(head)
    print()
    print(sum1(head))
    print(sum2(head))
    print(length(head))
    # head = reverseSll(head)
    # traverse(head)
