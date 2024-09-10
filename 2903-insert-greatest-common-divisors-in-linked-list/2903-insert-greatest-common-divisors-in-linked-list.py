# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        prev,curr=head,head.next
        while curr:
            gcd_node=ListNode(gcd(prev.val,curr.val))
            temp=prev.next
            prev.next=gcd_node
            gcd_node.next=curr

            prev=curr
            curr=curr.next
        return head






        def GCD(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)

        