# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        def InOrder(node, element):
            if node is None:
                return
            InOrder(node.left, element)
            element.append(node.val)
            InOrder(node.right, element)

        ele = []
        InOrder(root,ele)

        left, right = 0, len(ele)-1
        while left<right:
            curr = ele[left]+ele[right]
            if curr == k:
                return True
            elif curr<k:
                left+=1
            else:
                right-=1

        return False

