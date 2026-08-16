class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        string = s.lower()
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True