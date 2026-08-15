class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i, n in enumerate(nums):
            if target - n in hashy:
                return [hashy[target - n], i]
            hashy[n] = i
        return []