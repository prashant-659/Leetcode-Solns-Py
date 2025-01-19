class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        if not height or not height[0]:
            return 0


        R=len(height)
        C=len(height[0])

        if R<3 or C<3:
            return 0

        minHeap=[]
        for r in range(R):
            for c in range(C):
                if  r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    heappush(minHeap, (height[r][c],r,c))
                    height[r][c]=-1 #incocates visited


        res=0
        maxH=0
        while minHeap:
            h, r, c =heappop(minHeap)
            maxH=max(h, maxH)
            

            neighbors=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr, nc in neighbors:
                if (nr <0 or nc<0 
                    or nr ==R or 
                    nc==C or height[nr][nc]==-1):
                    continue
                heappush(minHeap,(height[nr][nc], nr, nc))
                if height[nr][nc]<maxH:
                    res+=maxH-height[nr][nc]
                height[nr][nc]=-1
                
        return res
                


        


                    