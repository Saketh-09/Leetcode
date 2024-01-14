class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row1 = 1
        m,n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        row1 = 0
                    else:
                        matrix[row][0] = 0
        for row in range(1,m):
            if matrix[row][0] == 0:
                for col in range(1,n):
                    matrix[row][col] = 0
        for col in range(n):
            if matrix[0][col] == 0:
                for row in range(1,m):
                    matrix[row][col] = 0
        if row1 == 0:
            for col in range(n):
                matrix[0][col] = 0

