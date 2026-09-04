class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        x = amount
        def dfs(amount):
            if amount == 0:
                return amount
            if amount in memo:
                return memo[amount]
            res = x + 1
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            memo[amount] = res
            return res
        res_coins = dfs(amount)
        return res_coins if res_coins < (x + 1) else -1
        
            