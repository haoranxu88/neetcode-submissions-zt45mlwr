class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # q up all of the treasure chest coordinates, then bfs from each treasure chest
        inf = 2**31 - 1
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        distance = 0
        while q:
            n = len(q)
            for x in range(n):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == inf:
                        grid[nr][nc] = distance + 1
                        q.append((nr, nc))
            distance += 1
        
            