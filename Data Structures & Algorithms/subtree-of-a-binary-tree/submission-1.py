# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def dfs(node):
            if not node:
                return
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    self.res = True
                    return
            dfs(node.left)
            dfs(node.right)
            return

        def sameTree(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return sameTree(a.left, b.left) and sameTree(a.right, b.right)
            else:
                return False
        dfs(root)
        return self.res