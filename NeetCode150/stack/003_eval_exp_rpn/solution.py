class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = ['+','-','*','/']
        stack = []
        result = 0
        for i in tokens:
            if i in operations:
                if i == '+':
                    result = stack.pop() + stack.pop()
                elif i == '-':
                    a, b = stack.pop(), stack.pop()
                    result = b - a
                elif i == '*':
                    result = stack.pop() * stack.pop()
                elif i == '/':
                    a, b = stack.pop(), stack.pop()
                    result = int(float(b)/a)
                print(result)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]

