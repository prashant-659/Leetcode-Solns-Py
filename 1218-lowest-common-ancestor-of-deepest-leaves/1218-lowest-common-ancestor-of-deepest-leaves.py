# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            d1, n1 = dfs(node.left)
            d2, n2  = dfs(node.right)

            if d1==d2:
                return d1+1, node
            elif d1>d2:
                return d1+1,  n1
            else:
                return d2+1, n2
        d, n=dfs(root)
        return n
            