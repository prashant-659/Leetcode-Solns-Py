# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        curr=root
        def trav(node):
            nonlocal res
            if not node:
                return

            trav(node.left)
            res.append(node.val)
            trav(node.right)

        trav(root)
        return res

