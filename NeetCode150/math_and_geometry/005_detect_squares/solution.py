from collections import defaultdict


class DetectSquares(object):

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.pts[tuple(point)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        pX, pY = point
        count = 0
        for x, y in self.pts.keys():
            if abs(pX - x) == abs(pY - y) and pX != x and pY != y:
                count += self.pts[(x, pY)] * self.pts[(pX, y)] * self.pts[(x, y)]
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)