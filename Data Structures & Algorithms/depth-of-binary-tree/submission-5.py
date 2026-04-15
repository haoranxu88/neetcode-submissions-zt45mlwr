# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(node, height):
            if not node:
                return
            height += 1
            self.res = max(self.res, height)
            depth(node.left, height)
            depth(node.right, height)
            return
        height = 0
        depth(root, height)
        return self.res
