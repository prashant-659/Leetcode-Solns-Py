# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr=[]
        def dfs(root):
            nonlocal arr
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        add=0
        for i in range(len(arr)):
            if arr[i]>=low and arr[i]<=high:
                add+=arr[i]
        return add