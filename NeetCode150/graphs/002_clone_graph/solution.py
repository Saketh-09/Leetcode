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
        q = collections.deque()
        q.append(node)
        print(type(node))
        res = []
        visited = set()
        while q:
            r = []
            n = q.popleft()
            visited.add(n)
            for nod in n.neighbors:
                if nod not in visited:
                    q.append(nod)
                    r.append(nod.val)
            res.append(r)
        return res
