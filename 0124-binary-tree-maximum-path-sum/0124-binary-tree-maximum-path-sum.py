# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res=root.val

        def dfs(root):
            curr_sum=0
            if not root:
                return 0
            
            
            left_max=dfs(root.left)
            right_max=dfs(root.right)

            nonlocal res

            res=max(res,root.val+left_max+right_max)
            return max(0,root.val+max(left_max, right_max))
        dfs(root)
        return res
            
