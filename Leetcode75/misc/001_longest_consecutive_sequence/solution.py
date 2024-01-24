class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ml = 0
        hashSet = {}
        for i in nums:
            hashSet[i] = False
        for i in hashSet:
            if not hashSet[i]:
                l = 1
                left = i-1
                while left in hashSet:
                    l+=1
                    hashSet[left] = True
                    left -= 1
                right = i+1
                while right in hashSet:
                    l+=1
                    hashSet[right] = True
                    right += 1
                ml = max(l,ml)
            hashSet[i] = True
        return ml