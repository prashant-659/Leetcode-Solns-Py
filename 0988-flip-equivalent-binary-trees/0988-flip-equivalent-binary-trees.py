# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # def dfs(node1,node2):
        #     if not node1 and not node2:
        #         return True
        #     if  not node1 and node2:
        #         return False
        #     if not node2 and node1:
        #         return False
        #     if node1 and node2:
        #         if node1.val==node2.val:
        #             return True
        #         if node1.left.val==node2.right.val:
        #             return True
        #         if node1.right.val==node2.left.val:
        #             return True
        #         if node1.left.val==node2.left.val:
        #             return True
        #         if node1.right.val==node2.right.val:
        #             return True
        #     return False
        #     return dfs(node1,node2) and dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
        # return dfs(root1,root2)
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val!=root2.val:
            return False
        a= self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
        return a or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)

