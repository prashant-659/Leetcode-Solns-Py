# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache={}
        def dfs(n):
            if n%2==0:
                return []
            if n==1:
                root=TreeNode(0)
                return [root]

            if n in cache:
                return cache[n]
            res=[]
            for i in range(1,n,2):
                left=dfs(i)
                right=dfs(n-i-1)
                
                for l in left:
                    for r in right:
                        root=TreeNode(0)
                        root.left=l
                        root.right=r
                        res.append(root)
                
            cache[n]=res
            return res

        return dfs(n)