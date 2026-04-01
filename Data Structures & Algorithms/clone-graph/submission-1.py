"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldnew = {}

        def dfs(n):
            if n in oldnew:
                return oldnew[n]
            copy = Node(n.val)
            oldnew[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None