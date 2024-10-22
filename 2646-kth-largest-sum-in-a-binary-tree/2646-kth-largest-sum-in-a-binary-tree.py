# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
            q=deque()
            res=[]
            q.append(root)
            while q:
                level_sum=0

                for i in range(len(q)):
                    cur=q.popleft()
                    level_sum+=cur.val

                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                heapq.heappush(res, level_sum)

                if len(res)>k:
                    heapq.heappop(res)
            return -1 if len(res)<k else res[0]
