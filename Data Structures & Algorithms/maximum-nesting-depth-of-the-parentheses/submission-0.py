class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
                res = max(res, len(stack))
            elif c == ')':
                stack.pop()
        return res
