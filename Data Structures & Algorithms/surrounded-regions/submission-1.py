class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # think about it like do not capture all unsurrounded regions
        # loop through perimeter, dfs and mark all connected parts as T
        # loop through and if 'O' then change to 'X' if 'T' then 'O'
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'