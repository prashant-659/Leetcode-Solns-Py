class Solution:
    def baseNeg2(self, n: int) -> str:
        base, ans=-2, ''
        while n!=0:
            n,r=divmod(n,base)
            if r<0:
                n,r=n+1,r-base
            ans=str(r)+ans
        return max(ans,"0")