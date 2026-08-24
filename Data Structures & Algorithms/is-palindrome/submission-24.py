class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            while not s_lower[l].isalnum() and l < r:
                l += 1
            while not s_lower[r].isalnum() and l < r:
                r -= 1
            if s_lower[l] == s_lower[r]:
                l += 1
                r -= 1
            else:
                return False
        return True