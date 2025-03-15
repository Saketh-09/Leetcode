# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        prev = d_node = ListNode(-1, head)
        node = head
        while node and node.next:
            t = node.next
            node.next = node.next.next
            prev.next = t
            t.next = node
            prev = node
            node = node.next
        return d_node.next