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
        if not node:
            return
        created = {}
        q = collections.deque([node])
        created[node.val] = Node(val=node.val)
        while q:
            n = q.popleft()
            copy = created[n.val]
            for neighbor in n.neighbors:
                if neighbor.val not in created.keys():
                    q.append(neighbor)
                    created[neighbor.val] = Node(neighbor.val)
                copy.neighbors.append(created[neighbor.val])
        return created[node.val]

