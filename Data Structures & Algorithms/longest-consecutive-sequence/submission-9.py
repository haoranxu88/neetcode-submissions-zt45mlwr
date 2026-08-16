class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        res = 1
        for n in nums:
            # if n - 1 exists, continue
            # if n - 1 does not exist, do a while loop 
            if n - 1 in s:
                continue
            curr_count = 1
            curr_num = n
            while curr_num + 1 in s:
                curr_count += 1
                curr_num += 1
                res = max(res, curr_count)
        return res