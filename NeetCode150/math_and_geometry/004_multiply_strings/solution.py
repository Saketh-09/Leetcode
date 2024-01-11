class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1)
        m = len(num2)
        res = [0] * (n + m)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(n):
            for j in range(m):
                product = int(num1[i]) * int(num2[j])
                res[i + j] += product
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, beg = res[::-1], 0
        while beg < (n + m) and res[beg] == 0:
            beg += 1
        res = "".join(map(str, res[beg:]))
        return '0' if res == '' else res
