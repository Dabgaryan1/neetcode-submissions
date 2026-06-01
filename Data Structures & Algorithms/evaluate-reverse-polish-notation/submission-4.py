class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            x = 0
            y = 0
            if i == '+':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y + x)
            elif i == '-':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y - x)
            elif i == '*':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y * x)
            elif i == '/':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y / x)
            else:
                stack.append(i)
        return int(stack.pop())


