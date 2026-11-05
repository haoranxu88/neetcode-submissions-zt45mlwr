from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs through by level
        # start by appending treasure chests
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        distance = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        q.append((nr, nc))
            distance += 1
        