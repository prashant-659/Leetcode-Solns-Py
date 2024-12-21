# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        mp=defaultdict(int)
        def dfs(node):
            
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            total= left+right+node.val
            mp[total]+=1
            return total
        dfs(root)

        max_val=max(mp.values())

        ans=[]
        for v in mp.keys():
            if mp[v]==max_val:
                ans.append(v)
        return ans