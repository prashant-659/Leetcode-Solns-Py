# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        Hashset=set(nums)
        dummy=ListNode(0, head)
        

        prev=dummy
        #curr=head
        # while curr:
        #     if curr.val in Hashset:
        #         prev.next = curr.next
                
        #     else:
        #         prev=prev.next
                
        #     curr=curr.next
            

        # return dummy.next
        while prev.next:
            if prev.next.val in Hashset:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return dummy.next
            



        