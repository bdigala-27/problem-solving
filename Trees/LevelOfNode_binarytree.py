class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LevelOfNode(root, target):
    if root is None:
        return 0
    q=[]
    currLevel = 1
    q.append(root)
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node = q.pop(0)
            if node.data == target:
                return currLevel
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        currLevel+=1
    return 0

# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(6)

print(LevelOfNode(root, 6))

