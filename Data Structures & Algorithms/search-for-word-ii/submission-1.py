class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie from words
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
        # built trie from words
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(board)
        cols = len(board[0])
        res = set()
        seen = set()
        word = []
        def dfs(r, c, seen, node, word): 
            # if out of bounds or in seen or not in children of current trie node return

            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in seen or board[r][c] not in node.children:
                return
            letter = board[r][c]
            word.append(letter)
            joined = "".join(word)
            node = node.children[letter]
            if node.word:
                res.add(joined)

            seen.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, seen, node, word)
            
            seen.remove((r, c))
            word.pop()

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, seen, root, word)
        return list(res)

        