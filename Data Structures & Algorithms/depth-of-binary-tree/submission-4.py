# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, height):
            if not node:
                return
            height += 1
            self.res = max(self.res, height)
            dfs(node.left, height)
            dfs(node.right, height)
            return
        dfs(root, self.res)
        return self.res
            