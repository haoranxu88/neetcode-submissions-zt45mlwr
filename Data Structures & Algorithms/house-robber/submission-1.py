class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1, 1, 3, 3]
        #  0  1  2  3
        # for each house, you can choose to rob the house n + 2 or not 
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]