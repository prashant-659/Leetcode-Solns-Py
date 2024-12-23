# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # def dash_count(s, from):
        #     depth=0
        #     for i in range(from, len(s)):
        #         if s[i]=="-":
        #             depth+=1
        #         else:
        #             break

        #     return depth

        # mode=Dash
        # stack=[]
        # curNum=0
        # curDash=0
        # dashes_before
        # for c in traversal:

        #     if c.isnumeric():
        def parse(traversal):
            r=[]
            stack=[]
            cur_Dash=0
            cur_Num=0
            Num=0
            Dash=1
            mode=Dash

            for c in traversal:
                if c=="-":
                    if mode==Num:
                        r.append((cur_Dash, cur_Num))
                        cur_Num=0
                        cur_Dash=0
                    mode=Dash
                    cur_Dash+=1
                else:
                    mode=Num
                    cur_Num=cur_Num*10+int(c)
            r.append((cur_Dash, cur_Num))
        
            return r
        r=parse(traversal)

        stack=[]
        for dashes, number in r:
            node=TreeNode(number)
            if dashes>=len(stack):
                
                if len(stack)>0:
                    if stack[-1].left is None:
                        stack[-1].left=node
                    else:
                        stack[-1].right=node
                stack.append(node)
            else:
                while len(stack)>dashes:
                    stack.pop()
                if stack[-1].left is None:
                    stack[-1].left=node
                else:
                    stack[-1].right=node
                stack.append(node)
        return stack[0]


            

