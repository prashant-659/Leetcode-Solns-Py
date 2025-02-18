# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph=defaultdict(list)
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)

        qu = deque([(start, 0)])
        max_d=-1
        visit=set()
        visit.add(start)

        while qu:
            node, d=qu.popleft()
            max_d=max(max_d, d)
            for nei in graph[node]:
                if nei not in visit:
                    qu.append((nei,d+1))
                visit.add(nei)

        return max_d
            
            
