"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create new nodes in one pass, then assign adjacents in second pass
        if not node:
            return None
        old_to_new = {}
        def dfs(n):
            if n in old_to_new:
                return
            old_to_new[n] = Node(n.val)
            for neigh in n.neighbors:
                dfs(neigh)
            return
        dfs(node)

        for old, new in old_to_new.items():
            for neigh in old.neighbors:
                old_to_new[old].neighbors.append(old_to_new[neigh])
        return old_to_new[node]
            