class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(2, n):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]