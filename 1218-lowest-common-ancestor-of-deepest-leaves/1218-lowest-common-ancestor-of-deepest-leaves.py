# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         def dfs(root):
#             if not root:
#                 return 0, None
#             d1, n1=dfs(root.left)
#             d2, n2 = dfs(root.right) 
#             if d1==d2:
#                 return d1+1, root
#             elif d1>d2:
#                 return d1+1, n1
#             else:
#                 return d2+1, n2
#         d, n=dfs(root)
#         return n

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            if left_depth == right_depth:
                return (left_depth + 1, node)
            elif left_depth > right_depth:
                return (left_depth + 1, left_node)
            else:
                return (right_depth + 1, right_node)
        return dfs(root)[1]