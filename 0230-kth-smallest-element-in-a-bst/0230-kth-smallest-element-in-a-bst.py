# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        stack=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res[k-1]



        # def trav(node):
        #     if not node:
        #         return 

        #     trav(node.left)
        #     res.append(node.val)
        #     trav(node.right)
        # trav(root)
        # return res[k-1]