class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial cases: target < m (l < target < m), target > m (r > target > m)
        # nontrivial cases: target < m (target < r)
        # target > m (target > l)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1