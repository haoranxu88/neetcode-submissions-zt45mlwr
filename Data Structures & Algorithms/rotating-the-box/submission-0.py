class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == '*':
                    i = c - 1
        res = []
        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(boxGrid[r][c])
            res.append(col)
        return res
