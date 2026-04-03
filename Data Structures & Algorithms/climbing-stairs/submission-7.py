class Solution:
    def climbStairs(self, n: int) -> int:
        # you can get to the current step using the n - 1 or n - 2 step
        if n == 1:
            return 1
        s1 = 1
        s2 = 2
        curr = 2
        for _ in range(2, n):
            curr = s1 + s2
            s1 = s2
            s2 = curr
        return curr