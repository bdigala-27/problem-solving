# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        for _ in range(right-left):
            temp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = temp

        return dummy.next