class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i<j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
            for j in range(n//2):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[i][n-j-1]
                    matrix[i][n-j-1] = tmp