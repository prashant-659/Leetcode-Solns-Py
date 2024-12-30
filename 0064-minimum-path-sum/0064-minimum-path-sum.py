class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Bottom up approach (True DP)
        # m=len(grid)
        # n=len(grid[0])

        # dp=[[0]*(n) for _ in range(m)]
        # dp[0][0]=grid[0][0]

        # for i in range(1, m):
        #     dp[i][0]=dp[i-1][0]+grid[i][0]
        # for j in range(1, n):
        #     dp[0][j]=dp[0][j-1]+grid[0][j]

        # for i in range(1, m):
        #     for j in range(1,n):
        #         dp[i][j]=grid[i][j]+min(dp[i-1][j], dp[i][j-1])
        # return dp[m-1][n-1]


        m=len(grid)
        n=len(grid[0])
        dp=[[-1] *(n) for _ in range(m)]
        dp[0][0]=grid[0][0]
        def min_steps(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i>0 and j>0:
                dp[i][j]=grid[i][j]+min(min_steps(i-1,j), min_steps(i,j-1))
            elif i==0 and j>0:
                dp[i][j]=grid[i][j]+min_steps(i, j-1)
            else:
                dp[i][j]=grid[i][j]+min_steps(i-1,j)
            return dp[i][j]
        return min_steps(m-1,n-1) 
