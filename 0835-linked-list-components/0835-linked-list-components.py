# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # mp=set(nums)
        # node=head
        # res=0
        # flag=False
        # while node: 
        #     if node.val not in mp and flag:
        #         res+=1
        #         flag=False
        #     elif node.val in mp:
        #         flag=True
        #     node=node.next
            
            
                 
        # if flag:
        #     res+=1
        # return res

        s=set(nums)
        ans=0
        node=head
        while node:
            if node.val in s and not(node.next and node.next.val in s):
                ans+=1
            node=node.next
        return ans
        
    
    
    

        