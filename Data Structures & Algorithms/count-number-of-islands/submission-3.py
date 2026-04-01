class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # process element
            grid[r][c] = '0'
            # process neighbors
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                else:
                    dfs(r, c)
                    res += 1
        return res