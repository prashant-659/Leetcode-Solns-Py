# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # node=root
        # while node:
        #     if node.val==val:
        #         return node
        #     if node.val<val:
        #         node=node.right
        #     else:
        #         node=node.left
        # return None
        # if not root:
        #     return None
        # if root.val==val:
        #     return root
        # elif root.val>val:
        #     self.searchBST(root.left, val)
        # else:
        #     self.searchBST(root.right, val)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)           
        else:
            return self.searchBST(root.right, val)
        
       

                