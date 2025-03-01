class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k>sum(candies):
            return 0

        def canuse(m):
            ct=0
            for p in candies:
                ct+=p//m
                
            return ct>=k

        r=max(candies)
        l=1
        while l<r:
            m=(l+r+1)//2
            if canuse(m):
                l=m
            else:
                r=m-1
        return r
        