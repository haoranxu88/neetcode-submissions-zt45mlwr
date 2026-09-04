class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
# case = [1, 5, 10] amount = 12
# 0                                                  12
# 1                              11                  7               2
# 2                    10        6      1      6     2          1
# 3              9     5    0   5 1    0    5   1   1        0
# return 3
        
# each node relies on the subproblem of remainder - coin for coin in coins
# when we hit remainder = 0 return 0
# memoize each time into memo
# if in memo we've already solved the subproblem and can return that
# otherwise we want to solve the subproblem
# we want the minimum amount, so there cannot be more than amount + 1 coins assuming lowest coin is 1
# set res = amount + 1, loop through every coin value to see if possible to make lower combination using dp
# memoize and return
        memo = {}
        x = amount
        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder in memo:
                return memo[remainder]
            res = x + 1
            for coin in coins:
                if remainder - coin >= 0:
                    res = min(res, 1 + dfs(remainder - coin))
            memo[remainder] = res
            return res
        coin_res = dfs(amount)
        return coin_res if coin_res < (x + 1) else -1










        # memo = {}
        # x = amount
        # def dfs(amount):
        #     if amount == 0:
        #         return amount
        #     if amount in memo:
        #         return memo[amount]
        #     res = x + 1
        #     for c in coins:
        #         if amount - c >= 0:
        #             res = min(res, 1 + dfs(amount - c))
        #     memo[amount] = res
        #     return res
        # res_coins = dfs(amount)
        # return res_coins if res_coins < (x + 1) else -1
        
            