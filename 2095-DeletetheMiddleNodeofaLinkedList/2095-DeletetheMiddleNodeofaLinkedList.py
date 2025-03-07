# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        slow = fast = head
        temp = head
        count = 0 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1

        for i in range(count-1):
            temp = temp.next

        temp.next = temp.next.next

        return head

        
        