# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1 for i in range(n)]  for i in range(m)]
        

        left, right=0,n-1
        top, bottom=0,m-1
        while head:
            
            #fill every value in top row
            for c in range(left, right+1):
                if head is None:  # Check if we've reached the end of the list
                    return mat
                mat[top][c]=head.val
                head=head.next
            top+=1
            #fill every value in right col
            for r in range(top, bottom+1):
                if head is None:  # Check if we've reached the end of the list
                    return mat
                mat[r][right]=head.val
                head=head.next
            right-=1

            #fill every val in bottom row( reverse ccol)
            for c in range(right, left-1,-1):
                if head is None:  # Check if we've reached the end of the list
                    return mat
                mat[bottom][c]=head.val
                head=head.next
            bottom-=1
            #fill every value in left col (reverse order)

            for r in range(bottom, top-1,-1):
                if head is None:  # Check if we've reached the end of the list
                    return mat
                mat[r][left]=head.val
                head=head.next
            left+=1
        return mat