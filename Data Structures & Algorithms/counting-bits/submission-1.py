class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n + 1):
            counts.append(bin(i).count('1'))
        return counts