class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i,c in enumerate(s):
            if c=='*':
                heappop(heap)
            else:
                heappush(heap,(c,-i))
        
        res = ['']*len(s)
        while heap:
            c,i = heappop(heap)
            res[-i] = c
            
        return ''.join(res)