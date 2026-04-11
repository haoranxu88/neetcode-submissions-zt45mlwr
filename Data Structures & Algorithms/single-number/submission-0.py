class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # same number xor itself becomes 0
        # xor every element
        res = 0
        for n in nums:
            res ^= n
        return res