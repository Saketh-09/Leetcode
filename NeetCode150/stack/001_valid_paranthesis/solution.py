class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(','}':'{',']':'['}
        for i in s:
            if len(stack) == 0 or i not in dict.keys():
                stack.append(i)
            elif stack[-1] == dict[i]:
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return 1
        else:
            return 0