class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tot = 0
        mult = 1
        for i in range(len(digits) - 1, -1, -1):
            tot += mult * digits[i]
            if mult == 1:
                tot += 1
            mult *= 10
        res = []
        while tot > 0:
            digit = tot % 10
            res.append(digit)
            tot = tot // 10
        return res[::-1]