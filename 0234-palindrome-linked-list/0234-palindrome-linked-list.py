# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums=[]
        curr=head
        while curr:
            nums.append(curr.val)
            curr=curr.next
        r=len(nums)-1
        for l in range(len(nums)):
            if nums[l]!=nums[r]:
                return False
            r-=1
        return True
