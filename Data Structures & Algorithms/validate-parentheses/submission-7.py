class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = set(['[', '(', '{'])
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if c == ']':
                    if not stack or stack.pop() != '[':
                        return False
                elif c == ')':
                    if not stack or stack.pop() != '(':
                        return False
                elif c == '}':
                    if not stack or stack.pop() != '{':
                        return False
        return True if not stack else False