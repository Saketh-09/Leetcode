# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkBalance(self,root):
        if not root:
            return 0, True
        lh, lb = self.checkBalance(root.left)
        rh, rb = self.checkBalance(root.right)
        if not lb or not rb or abs(lh-rh)>1:
            return 0, False
        return 1+max(lh,rh), True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, boolVal = self.checkBalance(root)
        return boolVal