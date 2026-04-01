class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, size):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            size[0] += 1
            print(size[0])
            for dr, dc in directions:
                dfs(r + dr, c + dc, size)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                else:
                    size = [0]
                    dfs(r, c, size)
                    res = max(res, size[0])
        return res