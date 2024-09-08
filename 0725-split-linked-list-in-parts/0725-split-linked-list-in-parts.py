# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res=[None]*k
        curr=head
        N=0
        while curr:
            N+=1
            curr=curr.next
        curr=head
        split_size=N//k
        num_remaining_part=N%k

        for i in range(k):
            newpart=ListNode(0)
            tail=newpart
            
            curr_size=split_size
            if num_remaining_part>0:
                num_remaining_part-=1
                curr_size+=1
            for j in range(curr_size):
                tail.next=ListNode(curr.val)
                tail=tail.next
                curr=curr.next
            res[i]=newpart.next
        return res
