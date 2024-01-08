class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits[-1] == 9:
            digits[-1] += 1
            return digits
        i = -1
        n = len(digits)
        while abs(i)<=n and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if abs(i) > n:
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits
