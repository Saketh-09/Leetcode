class Solution(object):
    def sumOfSquares(self,n):
        sum = 0
        while n:
            sum += (n%10)**2
            n //= 10
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
        if n==1:
            return True
        return False