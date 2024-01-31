class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m != n:
            return False

        hashMap = {}
        for i in range(0, n):
            if s[i] in hashMap.keys():
                hashMap[s[i]][0] += 1
            else:
                hashMap[s[i]] = [1, 0]

            if t[i] in hashMap.keys():
                hashMap[t[i]][1] += 1
            else:
                hashMap[t[i]] = [0, 1]

        for key, val in hashMap.items():
            if val[0] != val[1]:
                return False
        return True

