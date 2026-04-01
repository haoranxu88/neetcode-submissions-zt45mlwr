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
                if not stack or maps[stack.pop()] != c:
                    return False
        return len(stack) == 0
        