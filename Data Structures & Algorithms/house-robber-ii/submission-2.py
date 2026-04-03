class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(m):
            n = len(m)
            if n == 1:
                return m[0]
            if n == 2:
                return max(m[0], m[1])
            dp = [0] * n
            dp[0] = m[0]
            dp[1] = max(m[0], m[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], m[i] + dp[i - 2])
            return dp[-1]
        length = len(nums)
        case1 = nums[0:length - 1]
        case2 = nums[1:]
        a = rob1(case1)
        b = rob1(case2)
        return max(a, b)
