class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printAncestors(root,target):
    if root is None:
        return False
    if root.data == target:
        return True

    if (printAncestors(root.left,target) or printAncestors(root.right,target)):
        print(root.data,end =" ")
        return True

    return False


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

printAncestors(root, 7)
