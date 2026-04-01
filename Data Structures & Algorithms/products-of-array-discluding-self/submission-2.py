class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]* len(nums)
        post = [1]* len(nums)
        res = []
        for x in range(1, len(nums)):
            pre[x] = pre[x - 1] * nums[x - 1]
        for x in range(len(nums) - 2, -1, -1):
            post[x] = post[x + 1] * nums[x + 1]
        for x in range(len(nums)):
            res.append(pre[x] * post[x])
        return res