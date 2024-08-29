# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reversing 2nd half
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        prev=None

        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        #merge two halves
        first,second=head, prev

        while second:
            tmp1,tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first, second=tmp1, tmp2
            
            

    
