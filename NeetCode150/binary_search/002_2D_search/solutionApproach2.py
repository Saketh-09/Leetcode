class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        bottom = 0
        top = m - 1
        while top >= bottom:
            mid = (top+bottom)/2
            if matrix[mid][n-1] < target:
                bottom = mid+1
            elif matrix[mid][0] > target:
                top = mid-1
            else:
                break
        if top < bottom:
            return False
        l = 0
        r = n-1
        while l <= r:
            middle = (l+r)/2
            if matrix[mid][middle] < target:
                l = middle+1
            elif matrix[mid][middle] > target:
                r = middle-1
            else:
                return True
        return False
