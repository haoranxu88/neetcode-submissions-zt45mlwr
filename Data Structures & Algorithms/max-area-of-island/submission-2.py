class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, size):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            # handle node
            grid[r][c] = 0
            size[0] += 1
            for dr, dc in dirs:
                dfs(r + dr, c + dc, size)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = [0]
                    dfs(r, c, size)
                    res = max(res, size[0])
        return res
                
