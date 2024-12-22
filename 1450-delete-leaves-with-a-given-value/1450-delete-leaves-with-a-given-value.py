# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # q=deque([root])
        # while q:
        #     node=q.popleft()
        #     if node.val==target and not root.left and not root.right:
        #         node=None
        #     if node.left:
        #         q.append(root.left)
        #     if node.right:
        #         q.append(root.right)
        # return root

        if not root:
            return None
        root.left=self.removeLeafNodes(root.left, target)
        root.right=self.removeLeafNodes(root.right, target)
        if root.val==target and not root.left and not root.right:
            return None
        return root