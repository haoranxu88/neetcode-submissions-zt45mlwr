class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = defaultdict(int)
        ts = defaultdict(int)
        for x in range(len(s)):
            hs[s[x]] += 1
            ts[t[x]] += 1
        return hs == ts