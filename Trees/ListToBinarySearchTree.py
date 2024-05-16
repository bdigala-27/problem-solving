class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def ListToBST(nums):
    nums.sort()
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(mid)
    root.left = ListToBST(nums[:mid])
    root.right = ListToBST(nums[mid + 1:])

    return root


# Second Solution for the list to binary search tree
def ListToBST2(nums):
    return insertToBST(nums, 0, len(nums) - 1)


def insertToBST(nums, start, end):
    if start <= end:
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = TreeNode(nums,start, mid - 1)
        node.right = TreeNode(nums, mid + 1, end)
        return node
    else:
        return None
