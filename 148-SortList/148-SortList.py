# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()
        temp = head

        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next

        return head
            
        