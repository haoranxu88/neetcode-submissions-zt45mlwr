class Solution:
    def numDecodings(self, s: str) -> int:
        # 12 -> (1, 2) or (12)
        # 01 -> (0, 1) doesnt work and (01) doesnt work
        # leading 0 edge case makes invalid
        # max 26 (2 digits)
        # 126 -> (1, 2, 6) or (12, 6) or (1, 26)
        # 127 -> (1, 2, 7) or (12, 7)
        # 1012 -> (10, 1, 2) or (10, 12)
        # [1, 1, 1, 2]
        # if an index is 0 and prev index not 1 or 2, return 0
        # elif an index is 0 and pre index is 1 or 2, dp[index] = dp[index - 1]
        # for 126
        # [1, (n - 1) + 1 if <= 26]
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            prev = i - 1
            if s[i] == '0':
                if s[prev] == '1' or s[prev] == '2':
                    dp[i + 1] = dp[prev]
                else:
                    return 0
            else:
                if 10 <= int(s[prev:i+1]) <= 26:
                    dp[i + 1] = dp[prev] + dp[i]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]

        