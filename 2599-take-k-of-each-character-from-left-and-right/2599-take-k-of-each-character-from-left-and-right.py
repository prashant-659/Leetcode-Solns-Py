class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        # ct=[0,0,0]
        # for c in s:
        #     ct[ord(c)-ord("a")]+=1
        # if min(ct)<k:
        #     return -1
        
        # res=float("inf")

        # l=0 
        # for r in range(len(s)):
        #     ct[ord(s[r])-ord("a")]-=1
        #     while min(ct)<k:
        #         ct[ord(s[l])-ord("a")]+=1
        #         l+=1
        #     res=min(res,len(s)-(r-l+1))
        # return res

        freq=[0]*3
        size=len(s)
        for c in s:
            freq[ord(c)-ord("a")]+=1
        
        l,r=0,0
        if freq[0]<k or freq[1]<k or freq[2]<k:
            return -1
        for r in range(size):
            freq[ord(s[r])-ord("a")]-=1
            if freq[0]<k or  freq[1]<k or  freq[2]<k:
                freq[ord(s[l])-ord("a")]+=1
                l+=1
        return size-(r-l+1)




            
