class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # for each word/index in wordlist, map it to a length 26 array containing the number of letters at the ith index letter
        # iterate through each word, and check its array for difference, if total difference adding absolute difference at each 
        # index == 1 then they are undirected neighbors
        # bfs from beginword and once we hit endword, return the number of levels we traversed

        wordList.append(beginWord)

        graph = defaultdict(list)
        for i, word in enumerate(wordList):
            for j, word2 in enumerate(wordList):
                if i == j:
                    continue
                difference = 0
                for ind in range(len(word)):
                    if word[ind] != word2[ind]:
                        difference += 1
                print(difference)
                if difference == 1:
                    graph[word].append(word2)
                    graph[word2].append(word)
        print(graph)
        q = deque()
        q.append(beginWord)
        levels = 1
        visited = set()
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w in visited:
                    continue
                visited.add(w)
                if w == endWord:
                    return levels
                for neighbor in graph[w]:
                    q.append(neighbor)
            levels += 1
        return 0