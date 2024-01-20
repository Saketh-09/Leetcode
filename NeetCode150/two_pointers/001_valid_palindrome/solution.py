class Solution(object):
    def isAlNum(self,c):
        return (
            'A' <= c <= 'Z' or
            'a' <= c <= 'z' or
            '0' <= c <= '9'
        )
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        l = 0
        r = n-1
        while l<r:
            while l<r and not self.isAlNum(s[l]):
                l+=1
            while l<r and not self.isAlNum(s[r]):
                r-=1
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
