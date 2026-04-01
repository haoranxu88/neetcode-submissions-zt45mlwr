class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for x in range(len(nums) - 2):
            l = x + 1
            r = len(nums) - 1
            while l < r:
                if nums[x] + nums[l] + nums[r] == 0:
                    if (nums[x], nums[l], nums[r]) not in seen:
                        res.append([nums[x], nums[l], nums[r]])
                        seen.add((nums[x], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[x] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res
            
                