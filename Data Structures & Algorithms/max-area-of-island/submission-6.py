class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, size):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            size[0] += 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, size)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = [0]
                    dfs(r, c, size)
                    res = max(res, size[0])
        return res

