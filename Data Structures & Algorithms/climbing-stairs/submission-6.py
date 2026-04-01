class Solution:
    def climbStairs(self, n: int) -> int:
        # you can either come from the stair before or 2 stairs before
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return a