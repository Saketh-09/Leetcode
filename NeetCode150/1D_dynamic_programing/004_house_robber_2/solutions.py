class Solution(object):
    def h_robber_1(self, nums):
        n = len(nums)
        h1, h2 = 0,0
        for i in range(n):
            t = h2
            h2 = max(nums[i]+h1, h2)
            h1 = t
        return h2

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        return max(self.h_robber_1(nums[:-1]),self.h_robber_1(nums[1:]))