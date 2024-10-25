# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,d):
            if not node:
                return float("inf")
            if not node.left and not node.right:
                return d+1
            d+=1
            return min(dfs(node.left,d),dfs(node.right,d))
        if not root:
            return 0
        return dfs(root,0)
