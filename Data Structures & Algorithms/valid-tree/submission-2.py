class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is acyclic graph
        # create a mapped graph
        # if cycle (already visited) return False
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for n in graph[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True
        return dfs(0, None) and len(visited) == n