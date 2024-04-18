# This is the Navie approach for the Level Order Traversal algorithm
"""
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printCurrentLevel(root,i)
        
def printCurrentLevel(root,level):
    if root is None: return
    if level == 1: print(root.data, end = " ")
    elif level>1:
        printCurrentLevel(root.left,level-1)
        printCurrentLevel(root.right,level-1)
    
def height(root):
    if root == None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    
    if lheight >rheight:
        return lheight+1
    else:
        return rheight+1
        
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)
    
"""

# Optimized version of Level Order Traversal (Using QUEUE)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def LevelOrderTraversal(root):
    if root is None: return
    
    queue = []
    
    queue.append(root)
    
    while len(queue) > 0:
        print(queue[0].data, end = " ")
        root = queue.pop(0)
        
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
            
        
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print("Level order traversal of binary tree is -")
    LevelOrderTraversal(root)