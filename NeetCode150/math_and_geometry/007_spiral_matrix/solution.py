class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = t = 0
        m = len(matrix)
        n = len(matrix[0])
        r = n-1
        b = m-1
        res = []
        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            for j in range(t,b+1):
                res.append(matrix[j][r])
            r-=1
            if t<=b:
                for k in range(r,l-1,-1):
                    res.append(matrix[b][k])
                b-=1
            if l<=r:
                for p in range(b,t-1,-1):
                    res.append(matrix[p][l])
                l+=1
        return res