class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < left:
                left = prices[i]
            profit = max(profit, prices[i]-left)
        return profit