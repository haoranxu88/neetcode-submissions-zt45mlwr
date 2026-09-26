class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each index, you can choose to use it or not
        # when u choose to use it, append it to set
        # at base case, turn set into list and append to res

        res = []
        seen = set()

        def backtrack(index):
            # base case
            if index == len(nums):
                res.append(list(seen))
                return

            if nums[index] not in seen:
                seen.add(nums[index])
                backtrack(index + 1)
                seen.remove(nums[index])

            backtrack(index + 1)

        backtrack(0)

        return res
            