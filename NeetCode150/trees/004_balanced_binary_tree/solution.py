# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root):
        if not root:
            return (0, True)
        lh, lb = self.getHeight(root.left)
        rh, rb = self.getHeight(root.right)
        balanced = (lb and rb and abs(lh-rh)<=1)
        return (1+max(lh,rh), balanced)
    
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        h, b = self.getHeight(root)
        return b
        