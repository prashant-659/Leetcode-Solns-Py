# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        res=[]
        def inorder(root):
            nonlocal res
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        min_d=float("inf")
        for i in range(1,len(res)):
            min_d=min(min_d, res[i]-res[i-1])
        return min_d


