class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_depth(root, target):
    if root is None:
        return -1
    dist = -1
    if root.data == target:
        return dist + 1

    dist = find_depth(root.left, target)
    if dist >= 0:
        return dist + 1

    dist = find_depth(root.right, target)
    if dist>=0:
        return dist+1
    return dist


# Driver Code
if __name__ == '__main__':
    # Binary Tree Formation
    height = -1
    root = Node(5)
    root.left = Node(10)
    root.right = Node(15)
    root.left.left = Node(20)
    root.left.right = Node(25)
    root.left.right.right = Node(45)
    root.right.left = Node(30)
    root.right.right = Node(35)

    k = 25

    # Function call to find the
    # depth of a given node
    print("Depth: ", find_depth(root, k))