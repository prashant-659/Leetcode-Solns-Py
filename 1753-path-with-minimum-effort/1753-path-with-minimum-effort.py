class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R=len(heights)
        C=len(heights[0])

        minHeap=[[0,0,0]] # [diff,r,c]
        visit=set()
        dir=[[0,1],[0,-1],[1,0],[-1,0]]

        while minHeap:
            diff, r, c=heapq.heappop(minHeap)

            if (r, c) in visit:
                continue
            visit.add((r,c))
            if (r, c)==(R-1, C-1):
                return diff
            for dr, dc in dir:
                newR, newC=r+dr, c+dc
                if (newR<0 or newC<0 or newR==R or newC==C or 
                    (newR, newC) in visit):
                    continue
                newDiff=max(diff, abs(heights[r][c]-heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR,newC])


