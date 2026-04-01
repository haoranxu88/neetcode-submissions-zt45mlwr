class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = ['(', '{', '[']
        openers = set(o)
        for c in s:
            if c in openers:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            elif c == ')':
                if stack.pop() != '(':
                    return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
        return len(stack) == 0
