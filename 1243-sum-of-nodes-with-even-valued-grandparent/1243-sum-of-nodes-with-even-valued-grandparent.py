# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return
            nonlocal ans
            if parent and grandparent and grandparent.val&1==0:
                ans+=node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        ans=0
        dfs(root, None,None)
        return ans