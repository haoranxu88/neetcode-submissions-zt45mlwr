class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        # dp = [1, 2, 3, 5, 8]
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]
