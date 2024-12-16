class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]    
        for c in num:
            while k>0 and stack and stack[-1]>c:
                k-=1
                stack.pop()
            if not stack and c=="0":
                continue
            stack.append(c)
        
        res= "".join(stack)
        if k>0:
            res=res[:len(res)-k]
        return res if res else "0"
