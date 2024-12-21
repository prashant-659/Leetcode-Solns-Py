# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # q=deque([root])

        # res=[]

        # while q:
        #     level=len(q)
        #     max_val=float('-inf')
            
        #     for _ in range(level):
        #         node=q.popleft()
        #         max_val=max(max_val, node.val)

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(max_val)
        # return res

        res=[]
        def dfs(node, depth):
            if not node:
                return 
            
            if depth==len(res):
                res.append(node.val)
            else:
                res[depth]=max(res[depth], node.val)
            
            dfs(node.left,depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res
