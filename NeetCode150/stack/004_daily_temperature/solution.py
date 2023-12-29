class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        output = [0]*n
        stack = []
        for i in range(0,n):
            if not stack:
                stack.append([i,temperatures[i]])
            else:
                while stack[-1][1] < temperatures[i]:
                    index = stack[-1][0]
                    days = i - index
                    output[index] = days
                    stack.pop()
                    if not stack:
                        break
            stack.append([i,temperatures[i]])
        return output

