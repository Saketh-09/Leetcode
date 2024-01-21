class Solution(object):
    def twoSum(self, nums, i, target):
        res = []
        l = i
        r = len(nums)-1
        while l<r:
            if nums[l]+nums[r] > target:
                r -= 1
            elif nums[l]+nums[r] < target:
                l += 1
            else:
                res.append([nums[i-1],nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]<1:
                target = 0 - nums[i]
                triplets = self.twoSum(nums,i+1,target)
                res += triplets
        return res