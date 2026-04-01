class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # take shorter substring
        # take the size of it and create a sliding window of that size
        # if all the characters in that sliding window match the hashmap of the shorter subtring return true
        if len(s2) < len(s1):
            return False
        else:
            short = s1
            long = s2
        scounts = defaultdict(int)
        lcounts = defaultdict(int)
        for i in short:
            scounts[i] += 1
        n = len(short)
        for i in range(n - 1):
            lcounts[long[i]] += 1
        l = 0
        for r in range(n, len(long) + 1):
            lcounts[long[r - 1]] += 1
            if scounts == lcounts:
                return True
            lcounts[long[l]] -= 1
            if lcounts[long[l]] == 0:
                del lcounts[long[l]]
            l += 1
        return False
