class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        ct=[0,0,0]
        for c in s:
            ct[ord(c)-ord("a")]+=1
        if min(ct)<k:
            return -1
        
        res=float("inf")

        l=0 
        for r in range(len(s)):
            ct[ord(s[r])-ord("a")]-=1
            while min(ct)<k:
                ct[ord(s[l])-ord("a")]+=1
                l+=1
            res=min(res,len(s)-(r-l+1))
        return res

                



            
