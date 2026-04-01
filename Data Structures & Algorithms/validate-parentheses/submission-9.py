class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        maps = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in maps:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if maps[popped] != c:
                    return False
        return len(stack) == 0
        