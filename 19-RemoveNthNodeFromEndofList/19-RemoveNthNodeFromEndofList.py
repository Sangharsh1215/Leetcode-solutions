# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #begin

        if head.next is None:
            return None
        temp = head
        temp1 = head
        count = 0

        while temp:
            temp = temp.next
            count += 1
            x = count - n

        if x == 0:
            return head.next
        
        for i in range(x-1):
            temp1 = temp1.next

        temp1.next = temp1.next.next

        return head
