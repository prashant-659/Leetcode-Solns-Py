# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        mp=defaultdict(list)
        q=deque()
        q.append([root, 0])
        while q:
            node, level=q.popleft()
            mp[level].append(node.val)
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
        li=list(mp.values())

        for i in range(len(li)):
            rev=li[i][::-1]
            li[i]=rev if i%2 else li[i]
        return li