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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        

        def BT(val):
            if not val:
                return None
            m=len(val)//2
            node=TreeNode(val[m])
            node.left=BT(val[:m])
            node.right=BT(val[m+1:])
            return node
        return BT(arr)