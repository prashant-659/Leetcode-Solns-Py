class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n=len(prices)
       
        @cache
        def go(i, free):
            if i==n:
                return 0
            best=go(i+1, i+1)+prices[i]
            if free>0:
                best=min(best, go(i+1, free-1))
            return best
        return go(0,0)