class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        r1,r2 = 0,0
        for i in nums:
            t = max(r1+i,r2)
            r1 = r2
            r2 = t
        return r2