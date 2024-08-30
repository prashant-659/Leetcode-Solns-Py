# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque([root])
        #bfs is also called level order travrsal
        while q:
            len_q=len(q)
            rightSide=None

            for i in range(len_q):
                node=q.popleft()
                if node:
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res



        # res = []
        # def dfs(node, level):
        #     if not node:
        #         return
            
        #     if len(res) <= level:
        #         res.append(None)
            
        #     dfs(node.left, level+1)
        #     dfs(node.right, level+1)
        #     res[level] = node.val
        
        # dfs(root, 0)
        # return res

        




        # while root:
        #     val=root.val
        #     res.append(val)
        #     root=root.right
        # return res