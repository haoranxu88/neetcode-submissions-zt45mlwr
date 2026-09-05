class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True


    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.end
            if word[index] != '.':
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index + 1)
                else:
                    return False
            for char, tnode in node.children.items():
                if dfs(tnode, index + 1):
                    return True
            return False
        return dfs(self.head, 0)
            
