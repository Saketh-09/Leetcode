class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        subStringPointer = 0
        stringLength = len(t)
        subStringLength = len(s)
        if subStringLength == 0:
            return True
        for i in range(stringLength):
            if subStringPointer<subStringLength and t[i] == s[subStringPointer]:
                subStringPointer += 1
            if subStringPointer == subStringLength:
                return True
        else:
            return False
