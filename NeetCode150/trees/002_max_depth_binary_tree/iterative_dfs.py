# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        stack = []
        stack.append([root,1])
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append([node.right,depth+1])
                stack.append([node.left,depth+1])
                res = max(depth,res)
        return res

