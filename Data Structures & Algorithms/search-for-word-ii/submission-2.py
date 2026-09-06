# buid a trie out of the list of words
# dfs on each element of the grid, keeping track of visited nodes
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()
        for word in words:
            curr = head
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

        rows = len(board)
        cols = len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        # loop through each element in board, if in trie lvl 1, dfs through each adjacent element and checking
        # if in child of current trie node, keeping track of visited board elements and current word array
        # .join word array and append to res if full word returns
        visited = set()
        res = []
        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
                return
            char = board[r][c]
            if char not in node.children:
                return
            nxt = node.children[char]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, nxt)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, head)
        return res
            
            











            
        