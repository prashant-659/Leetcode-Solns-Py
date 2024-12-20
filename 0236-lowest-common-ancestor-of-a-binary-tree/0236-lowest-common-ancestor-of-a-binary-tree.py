# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, node1, node2):
            if root==None:
                return None
            if root==node1 or root==node2:
                return root
            left=lca(root.left, node1, node2)
            right=lca(root.right, node1, node2)

            if left!=None and right!=None:
                return root
            if not left and not right:
                return None
            
            return left if left else right

        return lca(root, p, q)       