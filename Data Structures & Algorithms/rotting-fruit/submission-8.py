class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            res += 1
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        return -1 if fresh > 0 else res