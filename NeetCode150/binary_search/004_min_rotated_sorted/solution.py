class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l<=r:
            m = l + (r-l)//2
            if nums[l] <= nums[r]:
                res = min(nums[l],res)
                break
            elif nums[l] <= nums[m]:
                l = m+1
            else:
                res = min(nums[m],res)
                r = m-1
        return res