class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        for i in range(0, len(new_str) // 2):
            if new_str[i] != new_str[len(new_str) - 1 - i]:
                return False
        return True