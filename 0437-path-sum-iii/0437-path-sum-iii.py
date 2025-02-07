# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curSum):
            if not node:
                return  0
            
            curSum+=node.val
            count=1 if curSum==targetSum else 0

            count+=dfs(node.left, curSum)
            count+=dfs(node.right, curSum)
            return count

        def outer_dfs(node):
            if not node:
                return 0
            return dfs(node, 0) + outer_dfs(node.left) + outer_dfs(node.right)
        
        return outer_dfs(root)
        
            
        

        
            

