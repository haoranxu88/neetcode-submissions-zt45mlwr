class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        txt = s.lower()
        while l < r:
            while not txt[l].isalnum() and l < r:
                l += 1
            while not txt[r].isalnum() and l < r:
                r -= 1
            if txt[l] != txt[r]:
                return False
            l += 1
            r -= 1
        return True
