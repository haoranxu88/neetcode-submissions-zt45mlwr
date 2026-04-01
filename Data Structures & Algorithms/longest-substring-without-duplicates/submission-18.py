class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        res = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res

        # chars = [d, v, f]
        # l = 1 r = 3 curr = 3
        # res = 3