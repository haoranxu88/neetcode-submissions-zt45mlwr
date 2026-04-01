class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
                continue
            total *= i
        prod = []
        for val in nums:
            if zero_count == 1:
                if val != 0:
                    prod.append(0)
                else:
                    prod.append(total)
            elif zero_count > 1:
                prod.append(0)
            else:
                prod.append(total // val)
        return prod