class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertBegin(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

        self.size += 1
    
    def insertEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.size += 1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

        self.size += 1

    def insertAtIndex(self, index, data):
        if index==0:
            self.insertBegin(data)
            return
        curr = self.head
        while curr and index > 1:
            curr = curr.next
            index -= 1

        if curr is None or index < 0:
            print("index out of range")
        else:
            newNode = Node(data)
            newNode.next = curr.next
            curr.next = newNode 
            self.size += 1

    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        if index < 0:
            print("index out of range")

        curr = self.head
        while curr and index > 1:
            curr = curr.next
            index -= 1
        
        if curr and curr.next:
            curr.next = curr.next.next            
            self.size -= 1
            return
        print("index out of range")

    def kth_element_from_last(self, k):
        left = right = self.head

        while k>1:
            right = right.next
            k -= 1
        
        if right is None or k < 1:
            print('out of range: (',0 ,' < position < ',self.size + 1,')' , sep='')
            return

        while right.next:
            right = right.next
            left = left.next
        
        print(left.data)
         
    # 5 5 6 5 5 4 5
    # 5 5 5
    def remove_all_nodes_with_data(self, data):
        if self.head == None:
            return

        while self.head and self.head.data == data:
            self.head = self.head.next
            self.size -= 1
        
        i = self.head
        prev = i
        while i:
            if i.data == data:
                while i and i.data == data:
                    i = i.next
                    self.size -= 1 
                prev.next = i
                prev = i
            else:
                i = i.next
                if i and i.data != data:
                    prev = i

    def remove_first_node_with_data(self, data):
        if self.head.data == data:
            self.deleteAtIndex(0)
            return 

        if self.size == 1:
            print('element not found')
            return 

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.size -= 1
                return 
            curr = curr.next

        print('element not found')
        
            
    def printSLL(self,msg=''):
        curr = self.head
        print(msg, end='', sep='')
        while(curr):
            print(curr.data, end=' ' if curr.next else '\n')
            curr = curr.next


a = SLL()
a.insertBegin(2)
a.insertBegin(3)
a.insertBegin(4)
a.insertEnd(5)
# a.printSLL()

a.insertAtIndex(4,1)
# a.printSLL()

a.deleteAtIndex(3)
a.printSLL()

a.kth_element_from_last(5)
a.remove_first_node_with_data(-9)
print()

a.insertEnd(3)
a.insertEnd(2)
a.insertEnd(3)
a.insertEnd(4)
a.insertEnd(4)

a.insertEnd(5)
a.insertEnd(5)
a.insertEnd(3)
a.insertEnd(5)
a.insertEnd(4)
a.insertEnd(5)
a.remove_all_nodes_with_data(5)
a.printSLL('after removing all 5\'s: ')
print('size:', a.size)
print()
a.remove_all_nodes_with_data(3)
a.printSLL('after removing all 3\'s: ')
print('size:', a.size)
print()
a.remove_all_nodes_with_data(3)
a.printSLL('after removing all 3\'s: ')
print('size:', a.size)
print()
a.remove_all_nodes_with_data(4)
a.printSLL('after removing all 4\'s: ')
print('size:', a.size)
