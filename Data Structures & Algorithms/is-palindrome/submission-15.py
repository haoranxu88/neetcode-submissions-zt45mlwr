class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        t = s.lower()
        while l < r:
            while not t[l].isalnum() and l < r:
                l += 1
            while not t[r].isalnum() and l < r:
                r -= 1
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True