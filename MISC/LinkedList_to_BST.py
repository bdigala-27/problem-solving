class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_middle(head):
    prev = None
    slow = head
    fast = head

    # Move fast pointer two steps and slow pointer one step until fast reaches the end
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect the left half from the mid node
    if prev:
        prev.next = None

    return slow


def sorted_list_to_bst(head):
    # Base cases
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    # Find the middle element
    mid = find_middle(head)

    # The middle element becomes the root
    root = TreeNode(mid.val)

    # Recursively construct the left subtree and right subtree
    root.left = sorted_list_to_bst(head)
    root.right = sorted_list_to_bst(mid.next)

    return root


# Helper function to print the tree in pre-order traversal
def pre_order_traversal(node):
    if not node:
        return []
    return [node.val] + pre_order_traversal(node.left) + pre_order_traversal(node.right)


# Example usage
# Create a sorted linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

# Convert the sorted linked list to a balanced BST
bst_root = sorted_list_to_bst(head)

# Print the pre-order traversal of the BST
print(pre_order_traversal(bst_root))
