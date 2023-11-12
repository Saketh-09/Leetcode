class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            swapPointer = i
            if nums[i] == 0:
                while swapPointer<n and nums[swapPointer] == 0:
                    swapPointer += 1
                if swapPointer<n:
                    tmp = nums[i]
                    nums[i] = nums[swapPointer]
                    nums[swapPointer] = tmp
