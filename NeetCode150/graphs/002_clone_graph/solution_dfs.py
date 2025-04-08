"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        created = {}
        def DFS(node):
            if node.val in created:
                return created[node.val]
            new_node = Node(val=node.val)
            created[node.val] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(DFS(n))
            return new_node
        return DFS(node) if node else None
