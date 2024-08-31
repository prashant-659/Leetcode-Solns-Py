# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inordIndex={v:i for i,v in enumerate(inorder)}
        def helper(l,r):
            if l>r:
                return None
            
            root = TreeNode(postorder.pop())
            idx = inordIndex[root.val] # Line A

            root.right = helper(idx+1, r) # Line B
            root.left = helper(l, idx-1) # Line C

            return root
        return helper(0, len(inorder)-1)