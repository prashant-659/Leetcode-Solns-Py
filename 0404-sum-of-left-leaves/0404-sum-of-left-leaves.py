# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # def dfs(node,sum, flag):
        #     if not node: return sum
        #     if node.left:
        #         flag=True
        #     if node.right:
        #         flag=False
        #     if flag and not node.left and not node.right:
        #         sum+=node.val
        #         return sum
            
                
        #     sum+=dfs(node.left,sum, flag)
        #     sum+=dfs(node.right,sum, flag)
        #     return sum
            

        def leftleaf(node, par):
            if not node: return 0
            if not node.left and not node.right:
                if par and par.left==node:
                    return node.val
            left=leftleaf(node.left, node)
            right=leftleaf(node.right, node)
            return left+right
        return leftleaf(root,None)
            



