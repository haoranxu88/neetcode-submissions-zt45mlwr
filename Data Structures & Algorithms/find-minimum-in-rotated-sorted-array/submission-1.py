class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mini = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            mid = (l + r) // 2
            mini = min(mini, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
        return mini
