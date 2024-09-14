# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        #BFS
        # level=0
        # q=deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node= q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # return level

        #DFS -- using stack
        # res=1
        # stack=[[root, 1]]
        # while stack:
        #     node,depth= stack.pop()
        #     if node:
        #         res=max(res,depth)
        #         stack.append([root.left,depth+1])
        #         stack.append([root.right,depth+1])
        # return res

        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)

            return 1+max(left, right)

        return dfs(root)




