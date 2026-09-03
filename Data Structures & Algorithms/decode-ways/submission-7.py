class Solution:
    def numDecodings(self, s: str) -> int:
# 1224

        #                                       i = 0
        #                   i = 1 (1)                               i = 2 (12)
        #       i = 2 (1, 2)            i = 3 (1, 22)           i = 3 (12, 2)   
#       i = 3 (1, 2, 2)  i = 4 (1, 2, 24)   i = 4 (1, 22, 4)           i = 4 (1, 22, 4)      i = 4 (12, 2, 4)  
# i = 4 (1, 2, 3, 4)

# if 0 then return 0
        memo = {}
        def dfs(i):
            # if we hit i = len(s) then we are end of that path of the tree
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            # any segment that starts with a 0 cannot continue
            if s[i] == '0':
                memo[i] = 0
                return 0
            plus_one = dfs(i + 1)
            plus_two = 0
            if (i + 2) <= len(s) and int(s[i:i+2]) <= 26:
                plus_two = dfs(i + 2)
            res = plus_one + plus_two
            memo[i] = res
            return res
        return dfs(0)
            