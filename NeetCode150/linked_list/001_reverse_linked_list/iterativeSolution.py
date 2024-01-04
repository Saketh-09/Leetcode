# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            next = head.next
            head.next = None
            while next != None:
                tmp = next.next
                next.next = head
                head = next
                next = tmp
        return head