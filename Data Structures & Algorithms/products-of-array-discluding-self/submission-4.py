class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, len(nums) - 1):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        res = []
        for i in range(len(nums)):
            if (i - 1) < 0:
                res.append(suffix[i + 1])
            elif (i + 1) >= len(nums):
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * suffix[i + 1])
        return res