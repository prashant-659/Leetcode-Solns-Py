class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n)] for j in range(m)]
        dp[0][0]=grid[0][0]

        def min_step(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            
        
            if i>0 and j>0:
                dp[i][j]=grid[i][j]+min(min_step(i-1,j),min_step(i,j-1))
                
            elif i==0 and j>0:
                dp[i][j]=grid[i][j]+min_step(i,j-1)
                
            else:
                dp[i][j]=grid[i][j]+min_step(i-1,j)
            return dp[i][j]
        return min_step(m-1,n-1)