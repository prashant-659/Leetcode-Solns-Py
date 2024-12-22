# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque([(root, 0)])
        max_level=float("-inf")
        while q:
            node, level=q.popleft()
            max_level=max(max_level, level)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right, level+1))
        print(level)


        val=0
        q=deque([(root, 0)])
        while q:
            node, level=q.popleft()

            if level==max_level:
                val+=node.val
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right, level+1))
        print(level)
        return val
         
            