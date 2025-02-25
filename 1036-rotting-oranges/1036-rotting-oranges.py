class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n =len(grid), len(grid[0])
        q=deque()
        fresh=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        time=0
        while q and fresh>0:
            for i in range(len(q)):
                r, c=q.popleft()
            

                for dr, dc in dir:
                    nr, nc=r+dr, c+dc
                    if nr==m or nc==n or nr<0 or nc<0 or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc]=2
                    q.append((nr, nc))
                    fresh-=1    
                
                
            time+=1
        return time if fresh==0 else -1
