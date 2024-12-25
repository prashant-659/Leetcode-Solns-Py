# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # subtrees=defaultdict(list)
        # def dfs(node):
        #     nonlocal res
        #     if not node:
        #         return "null"
            
        #     s=",".join([str(node.val), dfs(node.left),dfs(node.right)])
        #     if len(subtrees[s])==1:
        #         res.append(node)
        #     subtrees[s].append(node)
        #     return s
        
        # res=[]
        # dfs(root)
        # return res
        
        subtrees=defaultdict(int)
        def serialize(root):
            if not root:
                return "N"
            else:
                res=(str(root.val)+","+serialize(root.left)+","+serialize(root.right))
            subtrees[res]+=1
            if subtrees[res]==2:
                ans.append(root)
            return res
        res=""
        ans=[]
        serialize(root)
        return ans
