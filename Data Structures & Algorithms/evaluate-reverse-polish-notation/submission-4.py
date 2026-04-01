class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        ops = set(['+', '-', '*', '/'])
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(t)
            elif t in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(a / b)
        return int(stack.pop())