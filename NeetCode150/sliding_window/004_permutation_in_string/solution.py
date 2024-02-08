class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m>n: return False
        l1 = [0]*26
        l2 = [0]*26
        matching = 0
        for i in range(m):
            l1[ord(s1[i])-ord('a')]+=1
            l2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            matching += 1 if l1[i]==l2[i] else 0
        for i in range(m,n):
            if matching == 26: return True
            l2[ord(s2[i])-ord('a')]+=1
            if l2[ord(s2[i])-ord('a')] == l1[ord(s2[i])-ord('a')]:
                matching += 1
            elif l2[ord(s2[i])-ord('a')]-1 == l1[ord(s2[i])-ord('a')]:
                matching -= 1
            l2[ord(s2[i-m])-ord('a')]-=1
            if l2[ord(s2[i-m])-ord('a')] == l1[ord(s2[i-m])-ord('a')]:
                matching += 1
            elif l2[ord(s2[i-m])-ord('a')]+1 == l1[ord(s2[i-m])-ord('a')]:
                matching -= 1
        if matching == 26: return True
        return False