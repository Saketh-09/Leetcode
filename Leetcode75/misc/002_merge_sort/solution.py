class Solution(object):
    def merge(self, nums, l, m, r):
        lp = l
        k = l
        rp = m + 1
        for i in range(l, r + 1):
            if lp <= m and (rp > r or nums[lp] < nums[rp]):
                self.dup[i] = nums[lp]
                lp += 1
            else:
                self.dup[i] = nums[rp]
                rp += 1
        for i in range(l, r + 1):
            nums[i] = self.dup[i]

    def mergesort(self, nums, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergesort(nums, l, m)
            self.mergesort(nums, m + 1, r)
            self.merge(nums, l, m, r)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.dup = nums[:]
        self.mergesort(nums, 0, len(nums) - 1)
        return nums
