class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ph = nums[0]
        for i in range(len(nums)):
            ph -= 1
            if ph<nums[i]:
                ph = nums[i]
            if ph==0:
                if i == len(nums)-1:
                    return True
                return False
        return True