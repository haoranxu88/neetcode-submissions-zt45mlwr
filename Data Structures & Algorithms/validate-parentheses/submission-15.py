class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        bracks = {'[':']', '(':')', '{':'}'}
        for c in s:
            if c in bracks:
                stack.append(c)
            else:
                if not stack or bracks[stack.pop()] != c:
                    return False
        return len(stack) == 0