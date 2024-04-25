class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreOrderTraversal(root):
    if root is None: return

    print(root.data, end=" ")
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    PreOrderTraversal(root)
