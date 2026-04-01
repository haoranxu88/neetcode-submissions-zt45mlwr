class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = nums[i] * pref[i - 1]
        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            suff[i] = nums[i] * suff[i + 1]
        res = []
        for i in range(n):
            if (i - 1) < 0:
                res.append(suff[i + 1])
            elif (i + 1) >= n:
                res.append(pref[i - 1])
            else:
                res.append(pref[i - 1] * suff[i + 1])
        return res