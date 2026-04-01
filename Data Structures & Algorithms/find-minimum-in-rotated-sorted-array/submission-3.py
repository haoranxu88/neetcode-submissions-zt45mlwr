class Solution:
    def findMin(self, nums: List[int]) -> int:
        # cases: r < m (move l to m + 1), m < r (move r to m - 1)
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m - 1] > nums[m] and nums[m + 1] > nums[m]:
                return nums[m]
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
