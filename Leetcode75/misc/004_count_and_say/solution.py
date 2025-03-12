class Solution(object):
    def rle(self, s):
        f = None
        ans = ""
        for i in s:
            if not f:
                f = i
                count = 1
            elif f == i:
                count += 1
            else:
                ans += str(count) + f
                f = i
                count = 1
        ans += str(count) + i
        return ans

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cas = "1"
        for i in range(1, n):
            cas = self.rle(cas)
        return cas
