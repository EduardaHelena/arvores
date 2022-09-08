class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def getArray(root):
    if not root:
        return []
    
    array = []
    if root.left:
        array.append(root.left)
        
    if root.right:
        array.append(root.right)
        
    return array
    
def levelOrder(root):
    xpto = str(root) + " "
    
    array = getArray(root)
    
    while len(array) > 0:
        array_2 = []
        for i in array:
            xpto += str(i) + " "
            array_2 = array_2 + getArray(i)
        array = array_2
    print(xpto)

tree = BinarySearchTree()
t = 7

arr = [40, 20, 60, 50, 70, 10, 30]

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)