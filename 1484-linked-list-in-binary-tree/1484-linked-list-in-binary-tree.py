# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        curr=head
        visit=[]

        def dfs(curr,node):
            if not curr:
                return True
            if not node or curr.val!=node.val:
                return False
            return (dfs(curr.next, node.left) or
                    dfs(curr.next, node.right)
            )
        if dfs(head,root):
            return True
        if not root: return False
        return (
            self.isSubPath(head,root.left) or
            self.isSubPath(head,root.right)

        )

        # def dfs(temp, curr):
        #     if not curr:
        #         return True

        #     if curr.val not in visit:
        #         return True
        #     temp=root
        #     visit.append(temp)
        #     if temp.val==curr.val:
        #         dfs(temp.left,curr.next)
        #         dfs(temp.right, curr.next)
        #     else: 
        #         visit.pop()
        #     return False
            
        # return dfs(root,head)

