class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float("-inf")
        sum = 0
        for i in nums:
            sum += i
            max_sum = max(sum, max_sum)
            if sum<0:
                sum=0
        return max_sum