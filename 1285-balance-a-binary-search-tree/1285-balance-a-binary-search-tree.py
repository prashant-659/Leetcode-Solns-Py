# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def inorder(root):
            if not root: return

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        arr=[]
        inorder(root)
        # q=deque([root])
        # arr=[]
        # while q:
        #     node=q.popleft()
        #     arr.append(node.val)
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        def binary_partition(arr, l,h):
            if l>h:
                return None
            m=l+int((h-l)/2)
            node=TreeNode(arr[m])
            
            node.left=binary_partition(arr, l, m-1)
            node.right=binary_partition(arr, m+1, h)
            return node
        return binary_partition(arr, 0, len(arr)-1)


