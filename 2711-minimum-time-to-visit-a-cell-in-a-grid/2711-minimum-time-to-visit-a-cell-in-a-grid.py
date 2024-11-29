class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        q=[(0,0,0)]
        #time, row, col
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visit=[[False]*len(grid[0]) for _ in range(len(grid))]

        dir=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            t, r, c=heapq.heappop(q)
            
            if r==len(grid)-1 and c==len(grid[0])-1:
                    return t
            if visit[r][c]:
                continue
            visit[r][c]=True
            for dr, dc in dir:
                nr,nc=r+dr,c+dc
                
                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or visit[nr][nc]:
                    continue
                waiting=(grid[nr][nc]-t)%2==0

                new_t=max(grid[nr][nc]+waiting, t+1)
                heapq.heappush(q, (new_t, nr, nc))
        return -1

                    


