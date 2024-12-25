# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val, left=root)
        
        q=deque([root])
        for _ in range(depth-2):
            for _ in range(len(q)):
                node=q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        while q:
            node=q.popleft()
            node.left=TreeNode(val, left=node.left)
            node.right=TreeNode(val, right=node.right)
        return root