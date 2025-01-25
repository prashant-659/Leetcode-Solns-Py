class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod=1000000007
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*(n) for _ in range(m)]
        
        def dfs(r,c ,parent):
            if r<0 or r==m or c<0 or c==n or grid[r][c]<=parent:
                return 0
            if dp[r][c]!=-1:
                return dp[r][c]
            down=dfs(r+1,c,grid[r][c])
            up=dfs(r-1,c,grid[r][c])
            right=dfs(r,c+1,grid[r][c])
            left=dfs(r,c-1,grid[r][c])

            dp[r][c]=(1+left+right+up+down)%mod
            return (dp[r][c])
        count=0
        for r in range(m):
            for c in range(n):
                count=(count+dfs(r,c,-1))%mod
        return count




