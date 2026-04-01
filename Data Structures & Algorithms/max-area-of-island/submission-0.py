class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, count):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            count[0] += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc, count)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = [0]
                    dfs(r, c, count)
                    res = max(res, count[0])
        return res