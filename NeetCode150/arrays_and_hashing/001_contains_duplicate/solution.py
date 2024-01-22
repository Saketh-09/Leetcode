class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            else:
                hashSet.add(i)
        return False