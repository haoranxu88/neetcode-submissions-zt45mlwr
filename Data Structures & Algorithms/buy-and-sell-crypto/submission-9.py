class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0
        l = 0
        r = 1
        max_prof = 0
        prof = 0
        while (r < len(prices)):
            prof = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
            elif prof > max_prof:
                max_prof = prof
                r += 1
            else:
                r += 1
        return max_prof

        