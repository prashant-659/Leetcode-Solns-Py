# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def leaf_to_root(node,curr):
            if not node:
                return 0
            curr=curr*10+node.val
            if not node.left and not node.right:
                return curr
            l=leaf_to_root(node.left,curr)
            r=leaf_to_root(node.right,curr)

            return l+r

        return leaf_to_root(root,0)