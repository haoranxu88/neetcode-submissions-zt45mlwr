class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = defaultdict(int)
        for i, x in enumerate(nums):
            diff = target - x
            if diff in prevs:
                return [prevs[diff], i]
            prevs[x] = i
        return []
