# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=ListNode()
        # res=dummy
        # total=carry=0


        # while l1 is not None or l2 is not None or carry!=0:
        #     total=carry
        #     if l1:
        #         total+=l1.val
        #         l1=l1.next
        #     if l2:
        #         total+=l2.val
        #         l2=l2.next
        #     num=total%10
        #     carry=total//10
        #     dummy.next=ListNode(num)
        #     dummy=dummy.next
        # return res.next

        dummy=ListNode()
        cur=dummy
         
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            #new digit
            val=v1+v2+carry
            carry=val//10
            val=val%10
            cur.next=ListNode(val)

            #updte ptrs
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
