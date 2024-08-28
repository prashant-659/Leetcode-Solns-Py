class Solution:
    def trap(self, h: List[int]) -> int:
        if not h: return 0
        l,r=0,len(h)-1
        res=0
        max_l,max_r=h[l],h[r]
        while l<r:
            if max_l<max_r:
                l+=1
                max_l=max(max_l,h[l])
                res+=max_l-h[l]
            else:
                r-=1
                max_r=max(max_r,h[r])
                res+=max_r-h[r]
        return res
            
