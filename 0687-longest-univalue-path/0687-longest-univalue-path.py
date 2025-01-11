# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=[0]
        def dfs(node, parent):
            if not node:
                return 0
            
            l=dfs(node.left, node)
            r=dfs(node.right, node)

            res[0]=max(res[0],l +r)

            if parent and parent.val==node.val:
                return max(l,r)+1
            return 0
        dfs(root, None)
        return res[0]
        