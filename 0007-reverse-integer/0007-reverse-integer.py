class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        flag=False
        if s[0]=='-':
            s=s[1:]
            flag=True
        if flag:
            s='-'+s[::-1]
            return 0  if int(s)<(-2**31) else int(s)
        else:
            return 0 if int(s[::-1])>(2**31-1) else int(s[::-1])
        
