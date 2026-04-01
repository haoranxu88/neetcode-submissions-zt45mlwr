from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # implement a queue starting from all rotten fruits
        # we want to bfs each layer in each minute
        # once the queue is empty, we have finished
        # if there are zero fresh fruits return 0 else if fresh fruits exist and rottens dont return -1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        rot = 0
        def rotten(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] != 1:
                return
            q.append((r, c))
            visited.add((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rot += 1
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        elif fresh > 0 and rot == 0:
            return -1
        time = -1
        while q:
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] == 2 # turn rotten
                fresh -= 1
                for dr, dc in directions:
                    rotten(r + dr, c + dc)
        if fresh + rot == 0:
            return time
        else:
            return -1