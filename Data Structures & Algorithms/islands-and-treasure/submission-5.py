class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        path = 1
        seen = set()
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                seen.add((r, c))
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr, nc) in seen:
                        continue
                    if grid[nr][nc] == 2147483647:
                        q.append((nr, nc))
                        grid[nr][nc] = path
            path += 1
        
                