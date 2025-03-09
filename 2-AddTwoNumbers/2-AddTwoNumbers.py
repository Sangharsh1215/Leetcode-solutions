# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        l = []

        temp1 = l1
        temp2 = l2
        carry = 0

        while temp1 or temp2:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0

            total = val1 + val2 + carry 
            carry = total//10

            l.insert(0, str(total % 10))

            if temp1: temp1 = temp1.next
            if temp2: temp2 = temp2.next

        if carry:
            l.insert(0,'1')

        new_node = None
        for num in l:
            newnode = ListNode(int(num))
            newnode.next = new_node
            new_node = newnode
        return new_node


        




        