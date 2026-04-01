class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        seen = set()
        length = 1
        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            if s[r] not in seen:
                seen.add(s[r])
            if r - l + 1 > length:
                length = r - l + 1
        return length
            