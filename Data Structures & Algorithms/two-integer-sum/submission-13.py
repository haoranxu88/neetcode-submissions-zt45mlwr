class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = defaultdict(int)
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in n:
                return [n[sub], i]
            n[nums[i]] = i
        return []