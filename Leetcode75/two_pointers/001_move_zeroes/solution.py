class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        snowBallSize = 0
        for i in range(n):
            if nums[i] == 0:
                snowBallSize += 1
            elif snowBallSize > 0:
                nums[i-snowBallSize], nums[i] = nums[i], nums[i-snowBallSize]