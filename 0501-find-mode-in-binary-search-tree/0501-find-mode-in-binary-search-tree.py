# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter=defaultdict(int)
        
        def dfs(node, counter):
            if not node:
                return
            counter[node.val]+=1
            dfs(node.left,counter)
            dfs(node.right, counter)
        
        
        dfs(root,counter)
        maxm=max(counter.values())
        ans=[]
        for key in counter:
            if counter[key]==maxm:
                ans.append(key)
        return ans
            