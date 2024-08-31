# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def valid(node, left, right):
        #     if not node:
        #         return True
        #     if not (node.val<right and node.val>left):
        #         return False
        #     return (valid(node.left,left, node.val) and
        #     valid(node.right, node.val, right))
        # return valid(root,float("-inf"),float("inf"))

        stack=[]
        res=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True

            
            