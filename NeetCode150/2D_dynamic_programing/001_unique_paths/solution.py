class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        b = [0]*n
        for i in range(m-1,-1,-1):
            r=0
            for j in range(n-1,-1,-1):
                if (i==m-2 and j==n-1) or (i==m-1 and j==n-2) or (i==m-1 and j==n-1):
                    r=1
                    b[j]=1
                else:
                    b[j] = r = r+b[j]
        return r