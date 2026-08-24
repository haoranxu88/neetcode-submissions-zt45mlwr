class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        x = set(nums)
        res = 1
        for n in nums:
            if (n - 1) in x:
                continue
            curr = n
            curr_count = 1
            while (curr + 1) in x:
                curr_count += 1
                res = max(res, curr_count)
                curr += 1
        return res