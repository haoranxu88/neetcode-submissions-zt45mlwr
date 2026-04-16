class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find amount of fresh fruit
        # bfs from rotten fruit, if q empty and fresh fruit > 0, return -1
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        mins = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q and fresh > 0:
            n = len(q)
            mins += 1
            for _ in range(n):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        return mins if fresh == 0 else -1
        