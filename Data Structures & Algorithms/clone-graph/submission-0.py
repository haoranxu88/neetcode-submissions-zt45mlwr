"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}
        def dfs(n):
            if n in copy:
                return copy[n]
            new_node = Node(n.val)
            copy[n] = new_node
            for nei in n.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node
        return dfs(node) if node else None