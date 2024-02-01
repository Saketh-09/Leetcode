class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -1*stones[0]
            v1 = heapq.heappop(stones)
            v2 = heapq.heappop(stones)
            if v1!=v2:
                heapq.heappush(stones,v1-v2)
        return 0