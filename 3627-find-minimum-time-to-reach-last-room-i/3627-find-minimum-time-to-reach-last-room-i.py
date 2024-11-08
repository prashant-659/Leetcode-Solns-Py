class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R=len(moveTime)
        C=len(moveTime[0])
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=[[False]*(C) for _ in range(R)]
        minHeap=[(0,0,0)] #time, row, col
        heapq.heapify(minHeap)
        while minHeap:
            time,r,c=heapq.heappop(minHeap)
            if r==R-1 and c==C-1:
                return time

            for dr, dc in dir:
                new_r,new_c=r+dr,c+dc

                if (new_r>=R or new_c>=C or new_r<0 or new_c<0 or visited[new_r][new_c]):
                    continue
                
                visited[new_r][new_c]=True
                heapq.heappush(minHeap, (max(time+1, moveTime[new_r][new_c]+1),new_r, new_c))
        
        return -1






