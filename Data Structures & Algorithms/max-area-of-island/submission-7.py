class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, area):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            area[0] += 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, area)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    a = [0]
                    dfs(r, c, a)
                    max_area = max(a[0], max_area)
        return max_area