# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDepthDiameter(self,root):
        if not root:
            return 0,0
        leftHeight, leftDia = self.getDepthDiameter(root.left)
        rightHeight, rightDia = self.getDepthDiameter(root.right)
        height = 1+max(leftHeight,rightHeight)
        diameter = max(leftHeight+rightHeight, leftDia, rightDia)
        return height, diameter

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height,diameter = self.getDepthDiameter(root)
        return diameter