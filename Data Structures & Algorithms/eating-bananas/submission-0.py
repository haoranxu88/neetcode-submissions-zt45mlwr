class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # take from range 1 to max(piles) and binary search each possible k through O(n) for each k
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res