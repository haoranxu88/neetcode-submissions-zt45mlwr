class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort, then while looping through nums, take l and r pointers and see if they all add up
        # this is O(n) while looping through
        # [-4, -1, -1, 0, 1, 2]
        #   l.  i.           r
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[i], nums[r]])
                    while (l + 1) < len(nums) and nums[l] == nums[l + 1] and l < r:
                        l += 1
                    while (r - 1) > -1 and nums[r] == nums[r - 1] and l < r:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
        return res

                

