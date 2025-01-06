class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for c in ops:
            if c not in set("CD+"):
                stack.append(int(c))
            if c=="C":
                if stack:
                    stack.pop()
            if c=="D":
                if stack:
                    stack.append(stack[-1]*2)
            if c=="+":
                if len(stack)>=2:
                    stack.append(stack[-1]+stack[-2])
        return sum(stack) if stack else 0
