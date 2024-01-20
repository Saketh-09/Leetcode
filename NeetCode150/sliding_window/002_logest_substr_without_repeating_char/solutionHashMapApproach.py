class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charInd = {}
        l = 0
        ml = 0
        for r in range(0, len(s)):
            if s[r] in charInd.keys() and charInd[s[r]] >= l:
                l = charInd[s[r]] + 1
            charInd[s[r]] = r
            ml = max(ml, r - l + 1)
        return ml


