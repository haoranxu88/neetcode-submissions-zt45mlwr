class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        hs = {}
        ht = {}
        for i in s:
            if i in hs:
                hs[i] += 1
            else:
                hs[i] = 1
        for i in t:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        return hs == ht