class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def max_depth(node):
    if node is None:
        return 0
    
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    
    return max(left_depth, right_depth)+1
    
# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

depth = max_depth(root)
print(f"Depth of the binary tree: {depth}")