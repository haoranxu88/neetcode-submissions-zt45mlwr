class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [[0,1], [0,2]]
        # 0:1,2 | 1:0 | 2:0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbors in graph[node]:
                if neighbors not in visited:
                    dfs(neighbors)
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res
