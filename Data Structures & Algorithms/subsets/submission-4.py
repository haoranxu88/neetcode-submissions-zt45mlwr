class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each index, you can choose to use it or not
        # when u choose to use it, append it to set
        # at base case, turn set into list and append to res

        res = []
        seen = []

        def backtrack(index):
            # base case
            if index == len(nums):
                res.append(seen.copy())
                return

            seen.append(nums[index])
            backtrack(index + 1)
            seen.pop()

            backtrack(index + 1)

        backtrack(0)

        return res
            