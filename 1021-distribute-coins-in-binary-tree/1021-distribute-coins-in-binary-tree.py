# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(node):
            if not node:
                return 0 # extra_coins
            l_coins=dfs(node.left)
            r_coins=dfs(node.right)

            coins=l_coins+r_coins+node.val-1
            self.res+=abs(coins)

            return coins
        dfs(root)
        return self.res
