class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        sum = 0
        prefix_count = collections.defaultdict(int)
        prefix_count[0]=1
        for i in nums:
            sum += i
            if sum-k in prefix_count:
                res+=prefix_count[sum-k]
            prefix_count[sum]+=1
        return res