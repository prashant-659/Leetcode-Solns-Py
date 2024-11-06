# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(t1,t2):
            if not t1 or not t2:
                return t1==t2
            if t1.val!=t2.val:
                return False
            return dfs(t1.left,t2.right) and dfs(t1.right, t2.left)
        return dfs(root.left,root.right)