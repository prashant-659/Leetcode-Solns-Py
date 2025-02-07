# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def pathsum(node, curSum, temp):
            if not node:
                return
            curSum+=node.val
            temp.append(node.val)
            # if leaf node

            if not node.left and not node.right:
                if curSum==targetSum:
                    res.append(list(temp))

            pathsum(node.left, curSum, temp)
            pathsum(node.right, curSum, temp)
            temp.pop() #backtrack
        pathsum(root, 0, [])
        return res
