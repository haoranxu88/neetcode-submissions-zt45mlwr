# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 1
        def dfs(node, count):
            if not node:
                return
            count += 1
            self.res = max(self.res, count)
            dfs(node.left, count)
            dfs(node.right, count)
            return
        dfs(root, 0)
        return self.res