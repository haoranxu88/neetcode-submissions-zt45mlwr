class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we can build two auxillary grids, one for pacific one for atlantic
        # we can bfs from each pacific edge and if the height is >= mark True
        # same thing for each atlantic edge
        # loop through every index and if True at that index for both 
        # auxillaries then we can return True
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)] # aux pacific
        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)] # aux atlantic

        pacific_q = deque()
        visited_pacific = set()

        atlantic_q = deque()
        visited_atlantic = set()

        def bfs(r, c, h, ocean):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < h:
                return
            if ocean == 'P' and (r, c) in visited_pacific:
                return
            if ocean == 'A' and (r, c) in visited_atlantic:
                return
            if ocean == 'P' and heights[r][c] >= h:
                pacific[r][c] = True
                pacific_q.append((r, c))
                visited_pacific.add((r, c))
            if ocean == 'A' and heights[r][c] >= h:
                atlantic[r][c] = True
                atlantic_q.append((r, c))
                visited_atlantic.add((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_q.append((r, c))
                    visited_pacific.add((r, c))
                    pacific[r][c] = True
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic_q.append((r, c))
                    visited_atlantic.add((r, c))
                    atlantic[r][c] = True
        
        while pacific_q:
            for p in range(len(pacific_q)):
                r, c = pacific_q.popleft()
                pacific[r][c] = True
                for dr, dc in directions:
                    bfs(r + dr, c + dc, heights[r][c], 'P')
        
        while atlantic_q:
            for p in range(len(atlantic_q)):
                r, c = atlantic_q.popleft()
                atlantic[r][c] = True
                for dr, dc in directions:
                    bfs(r + dr, c + dc, heights[r][c], 'A')

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] == True and atlantic[r][c] == True:
                    res.append([r, c])
        return res







