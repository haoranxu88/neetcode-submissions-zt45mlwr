class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        res = 0
        for n in s:
            if (n + 1) in s:
                continue
            num = n
            curr = 1
            while (num - 1) in s:
                num -= 1
                curr += 1
            res = max(res, curr)
        return res