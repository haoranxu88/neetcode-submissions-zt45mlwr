class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if (n - 1) in s:
                continue
            count = 1
            curr = n
            while (curr + 1) in s:
                count += 1
                curr += 1
            res = max(res, count)
        return res