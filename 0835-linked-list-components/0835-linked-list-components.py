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


        """Input:
Linked list: 0 -> 1 -> 2 -> 3 -> 4
nums = [0, 1, 3, 4]

Execution:
Convert nums to a set: s = {0, 1, 3, 4}.
Traverse the linked list:
Node 0: 0 in s and 1 in s → Continue (same component).
Node 1: 1 in s and 2 not in s → End of component → Increment ans to 1.
Node 2: 2 not in s → Skip.
Node 3: 3 in s and 4 in s → Continue (same component).
Node 4: 4 in s and curr.next is None → End of component → Increment ans to 2.
Output:
ans = 2"""
        
    
    
    

        