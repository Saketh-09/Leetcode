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
        prev = None
        def reverseRecursion(prev, head):
            if head:
                next = head.next
                head.next = prev
                prev = head
                head = next
                return reverseRecursion(prev,head)
            else:
                return prev
        return reverseRecursion(prev, head)