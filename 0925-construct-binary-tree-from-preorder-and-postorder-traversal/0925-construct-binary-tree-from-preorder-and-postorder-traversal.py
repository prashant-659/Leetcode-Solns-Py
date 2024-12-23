# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic={n:i for i, n in enumerate(postorder)}
        def dfs(pre, preStart, preEnd, post, postStart, posEnd):
            if preStart>preEnd: return None

            root=TreeNode(pre[preStart])
            if preStart==preEnd:
                return root

            postIndex= postStart
            # while post[postIndex]!=pre[preStart+1]: 
            #     postIndex+=1
            postIndex=dic[pre[preStart+1]]

            length=postIndex-postStart+1
            root.left=dfs(pre, preStart+1, preStart+length, post, postStart, postIndex)
            root.right=dfs(pre, preStart+length+1, preEnd, post, postIndex+1, posEnd-1)
            return root
        return dfs(preorder, 0, len(preorder)-1, postorder, 0, len(preorder)-1)

