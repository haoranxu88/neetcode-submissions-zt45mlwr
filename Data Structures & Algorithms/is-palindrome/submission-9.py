class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        lowercase = lowercase.replace(' ', '')
        for i in lowercase:
            if i.isalnum() == False:
                lowercase = lowercase.replace(i, '')
        backwards = len(lowercase) - 1
        for i in range(0, len(lowercase) // 2):
            if lowercase[i] != lowercase[backwards - i]:
                return False
        return True