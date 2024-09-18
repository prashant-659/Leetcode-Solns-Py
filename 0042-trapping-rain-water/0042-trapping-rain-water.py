class Solution:
    def trap(self, h: List[int]) -> int:
        # if not h: return 0
        # l,r=0,len(h)-1
        # res=0
        # max_l,max_r=h[l],h[r]
        # while l<r:
        #     if max_l<max_r:
        #         l+=1
        #         max_l=max(max_l,h[l])
        #         res+=max_l-h[l]
        #     else:
        #         r-=1
        #         max_r=max(max_r,h[r])
        #         res+=max_r-h[r]
        # return res
        n=len(h)
        max_l,max_r=[0]*n,[0]*n
        max_l[0]=h[0]
        max_r[-1]=h[-1]
        for i in range(1,n):
            max_l[i]=max(max_l[i-1],h[i])

        for i in range(n-2,-1,-1):
            max_r[i]=max(max_r[i+1],h[i])
        
        water=[0]*n
        for i in range(n):
            water[i]=min(max_r[i],max_l[i])-h[i]
        total=0
        for i in range(n):
            total+=water[i]
        return total



            
