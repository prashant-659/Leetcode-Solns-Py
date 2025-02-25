# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node,parent, depth, target):
            if not node:
                return None, -1
            if node.val==target:
                return parent, depth
            left, p=dfs(node.left, node,depth+1, target)
            if p!=-1:
                return left, p
            return dfs(node.right,node, depth+1, target)
        p1,l=dfs(root, None,0,x)
        p2,r=dfs(root, None,0,y)
        return p1 !=p2 and l==r


            