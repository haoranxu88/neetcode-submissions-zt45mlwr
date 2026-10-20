class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # []
        # [1] [2] [1]
        # [1 2] [1 1] [2 1] [2 1] [1 1] [1 2]
        # [1 2 1]
        # set of arrays

        res = set()
        def backtrack(x):
            # base case
            if x not in res:
                res.add(x)
            else:
                return

            if len(x) == 0:
                return

            for i in range(len(x)):
                tup = x[:i] + x[i + 1:]
                backtrack(tup)

        nums.sort()
        backtrack(tuple(nums))
        return [list(t) for t in res]