# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return None
        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length+=1

        lastElement.next = head
        k = k % length

        prev = head

        for _ in range(length-k-1):
            prev = prev.next

        answer = prev.next
        prev.next = None

        return answer


