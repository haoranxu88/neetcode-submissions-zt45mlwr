class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        distance = 1
        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == (2**31 - 1):
                        grid[nr][nc] = distance
                        q.append((nr, nc))
            distance += 1
        