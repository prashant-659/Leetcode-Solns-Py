class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l,r=1,max(quantities)

        res=r
        while l<=r:
            k=(l+r)//2
            hours=0
            for p in quantities:
                hours+=math.ceil(p/k)

            if hours<=n:       
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
