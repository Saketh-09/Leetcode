# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(-1,head)
        secPtr = node = dummyNode
        while n>0:
            secPtr = secPtr.next
            n-=1
        while secPtr.next:
            node = node.next
            secPtr = secPtr.next
        node.next = node.next.next
        return dummyNode.next