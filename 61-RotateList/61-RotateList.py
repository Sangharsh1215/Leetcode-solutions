# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        tail = head
        l = 1
        while tail.next:
            tail = tail.next
            l += 1

        k = k%l
        if k==0:
            return head
        n = l-k-1

        newtail = head
        for i in range(n):
            newtail = newtail.next

        newhead = newtail.next
        newtail.next = None

        tail.next = head

        return newhead
        