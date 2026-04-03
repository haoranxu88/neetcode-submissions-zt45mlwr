class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0 and (nums[i], nums[l], nums[r]) not in seen:
                    res.append([nums[i], nums[l], nums[r]])
                    seen.add((nums[i], nums[l], nums[r]))
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
            