class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        ret_list = []
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if j == i:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in indices and indices[target] != i and indices[target] != j and sorted([nums[i], nums[j], target]) not in ret_list:
                    ret_list.append(sorted([nums[i], nums[j], target]))
        return ret_list