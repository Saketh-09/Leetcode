class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countZ, countO, countT = 0, 0, 0
        for i in nums:
            if i == 0:
                countZ += 1
            elif i == 1:
                countO += 1
            elif i == 2:
                countT += 1
        i = 0
        while countZ > 0:
            nums[i] = 0
            i += 1
            countZ -= 1

        while countO > 0:
            nums[i] = 1
            i += 1
            countO -= 1

        while countT > 0:
            nums[i] = 2
            i += 1
            countT -= 1
