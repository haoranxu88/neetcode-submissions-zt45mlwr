class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each treasure chest with a queue
        q = deque()
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in seen or grid[r][c] == -1:
                return
            q.append((r, c))
            seen.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))
        distance = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
            
                for dr, dc in directions:
                    addRoom(r + dr, c + dc)
            distance += 1
        