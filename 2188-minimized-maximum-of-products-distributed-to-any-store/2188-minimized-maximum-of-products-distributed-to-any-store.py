class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l,r=0,max(quantities)

        while l+1<r:
            m=(l+r)//2
            if sum(ceil(i/m) for i in quantities)<=n:
                r=m
            else:
                l=m
        return r 
