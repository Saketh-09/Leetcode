class Solution(object):
    def partition(self, nums, l, h):
        p = nums[h]
        i = l - 1
        for j in range(l, h):
            if nums[j] < p:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[h] = nums[h], nums[i + 1]
        return i + 1

    def quick_sort(self, nums, l, h):
        if l < h:
            i = self.partition(nums, l, h)
            self.quick_sort(nums, l, i - 1)
            self.quick_sort(nums, i + 1, h)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums