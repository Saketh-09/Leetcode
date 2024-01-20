class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(0,len(nums)):
            if target - nums[i] in hashMap.keys():
                return [hashMap[target - nums[i]],i]
            hashMap[nums[i]] = i