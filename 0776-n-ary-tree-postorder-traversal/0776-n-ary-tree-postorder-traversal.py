"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Recursive 
        res=[]
        if not root: return []

        stack=[root]
        res=[]

        while stack:
            temp=stack.pop()
            res.append(temp.val)

            for child in temp.children:
                stack.append(child)
        return res[::-1]

        

       
