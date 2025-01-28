class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        visit=set()
        maxi=0
        def dfs(r,c):
            if r<0 or r==R or c<0 or c==C or (r, c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            res=grid[r][c]
            
            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            for dr, dc in dir:
                nr=r+dr
                nc=c+dc
                res+=dfs(nr, nc)
            return res
            
                
        res=0          
        for r in range(R):
            for c in range(C):
                if grid[r][c] and (r,c) not in visit:
                   res=max(res, dfs(r,c))
        return res
            
                           

            