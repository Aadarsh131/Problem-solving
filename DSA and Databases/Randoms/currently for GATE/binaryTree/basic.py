# Python program to demonstrate delete operation
# in binary search tree
 
# A Binary Tree Node
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
 
 
# A utility function to do inorder traversal of BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
 
# A utility function to insert a new node with given key in BST
def insert( node, key):
 
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
 
    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node
 
# Given a non-empty binary search tree, return the node
# with minum key value found in that tree. Note that the
# entire tree does not need to be searched 
def minValueNode( node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left 
 
    return current 
 
# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root 
 
    # If the key to be deleted is similiar than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
         
        # Node with only one child or no child
        if root.left is None :
            temp = root.right 
            root = None
            return temp 
             
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
 
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right , temp.key)
 
 
    return root 

def fn(root):
    if root == None: 
        return 0
    elif root.left == None and root.right == None: 
        return 2
    else: 
        x = 3 + fn(root.left) + fn(root.right)
        return x

def checkIfSameTree(root1, root2):
    if root1 == None and root2 == None:
        return 1
    if root1 == None or root2 == None:
        return 0
    return (root1.key == root2.key and checkIfSameTree(root1.left,root2.left) and checkIfSameTree(root1.right, root2.right))
# Driver program to test above functions
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """
 
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 90)

root2 = None
root2 = insert(root2, 50)
root2 = insert(root2, 30)
root2 = insert(root2, 20)
root2 = insert(root2, 40)
root2 = insert(root2, 70)
root2 = insert(root2, 60)
root2 = insert(root2, 80)


print(fn(root))
print(fn(root2))
print(f'Both trees are: {'Same' if checkIfSameTree(root,root2) else 'Not Same'}')

print('\npreorder: ', end=' ')
preorder(root)
print('\ninorder: ', end=' ')
inorder(root)
print('\npostorder: ', end=' ')
postorder(root)
'''
print("Inorder traversal of the given tree")
inorder(root)
 
print( "\nDelete 20")
root = deleteNode(root, 20)
print( "Inorder traversal of the modified tree")
inorder(root)
 
print ("\nDelete 30")
root = deleteNode(root, 30)
print( "Inorder traversal of the modified tree")
inorder(root)
 
print( "\nDelete 50")
root = deleteNode(root, 50)
print( "Inorder traversal of the modified tree")
inorder(root)
'''