# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return current max height and diameter
        def dfs(node):
            # base case null node height 0
            if not node:
                return 0, 0
            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)
            # result can be current diameter max found in subtree
            # or longest left subtree height + longest right subtree height
            # current height is max of left and right subtree heights + 1
            return (max(lh, rh) + 1, max(ld, rd, lh + rh))
        return dfs(root)[1]