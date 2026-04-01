class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        sequence = set()
        for r in range(len(s)):
            while s[r] in sequence:
                sequence.remove(s[l])
                l += 1
            sequence.add(s[r])
            res = max(res, r - l + 1)
        return res
