# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # nums=[]
        # curr=head
        # while curr:
        #     nums.append(curr.val)
        #     curr=curr.next
        # r=len(nums)-1
        # for l in range(len(nums)):
        #     if nums[l]!=nums[r]:
        #         return False
        #     r-=1
        # return True
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        curr=None
        hd=head
        while slow:
            nxt=slow.next
            slow.next=curr
            curr=slow
            slow=nxt
        while curr:
            if curr.val!=hd.val:
                return False
            curr=curr.next
            hd=hd.next
        return True