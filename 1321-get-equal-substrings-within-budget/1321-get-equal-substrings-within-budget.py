class Solution:
    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        prefix=[0]*len(s)
        for i in range(len(s)):
            prefix[i]=abs(ord(s[i])-ord(t[i]))
        l=0
        res=0
        for r in range(len(s)):
            cost-=prefix[r]
            if cost<0:
                cost+=prefix[l]
                l+=1
            res=max(res, r-l+1)
        return res
            

