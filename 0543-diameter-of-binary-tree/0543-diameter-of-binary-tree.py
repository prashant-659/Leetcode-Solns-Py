# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res=[0]

        # def dfs(root):
        #     if not root:
        #         return -1
            
        #     left=dfs(root.left)
        #     right=dfs(root.right)
        #     res[0]=max(res[0],2+left+right)

        #     return 1+max(left,right)

        # dfs(root)
        # return res[0]

        res=0
        def dfs(node):
            nonlocal res
            if not node: #Base
                return -1
            
            #Hypothesis
            l=dfs(node.left)
            r=dfs(node.right)

            #Inductions
            temp=1+max(l,r)
            ans=max(temp,2+l+r)
            res=max(res,ans)
            return temp
        dfs(root)
        return res
