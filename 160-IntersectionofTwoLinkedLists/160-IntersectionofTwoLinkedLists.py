# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp = headB

        while temp and temp.next:
            temp = temp.next
        if not temp:
            return None

        temp.next = headA

        slow,fast = headB,headB
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            temp.next = None  
            return None

        slow = headB
        while slow != fast:
            slow = slow.next
            fast = fast.next

        temp.next = None

        return slow


        