class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1 
        while l < r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                l = r = m

        row = l

        if target < matrix[row][0] or target > matrix[row][-1]:
                return False

        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
            
        
