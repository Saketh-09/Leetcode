class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cost.append(0)
        for i in range(2,n+1):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return cost[-1]