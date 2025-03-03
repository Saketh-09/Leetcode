# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = deque([(root, None)])
        while q:
            xParent, yParent = None, None
            s = len(q)
            for _ in range(s):
                node, parent = q.popleft()
                if node.val == x:
                    xParent = parent
                if node.val == y:
                    yParent = parent
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            if xParent and yParent:
                return xParent != yParent
            if xParent and not yParent or yParent and not xParent:
                return False