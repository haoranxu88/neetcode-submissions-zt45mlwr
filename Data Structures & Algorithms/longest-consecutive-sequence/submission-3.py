class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        snums = sorted(nums)
        longest_count = 1
        running_count = 1
        for i in range(1, len(nums)):
            if snums[i] - snums[i - 1] == 1:
                running_count += 1
            elif snums[i] - snums[i - 1] == 0:
                continue
            else:
                running_count = 1
            if running_count > longest_count:
                longest_count = running_count
        return longest_count