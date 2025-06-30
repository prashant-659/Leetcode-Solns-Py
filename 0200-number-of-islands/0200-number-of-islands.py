class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R=len(grid)
        C=len(grid[0])
        visit=set()
        ans=0
        def bfs(r,c):
            q=deque([(r,c)])
            dire=[(1,0),(-1,0),(0,1),(0,-1)]
            visit.add((r,c))
            while q:
                r,c=q.popleft()
                for dr, dc in dire:
                    nr,nc=r+dr, c+dc
                    if 0<=nr<R and 0<=nc<C and (nr,nc) not in visit and grid[nr][nc]=="1":
                        q.append((nr,nc))
                        visit.add((nr, nc))
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    ans+=1
        return ans
                    
        
                    
                    
            