class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m=len(obs)
        n=len(obs[0])
        dp=[[0] *(n+1) for _ in range(m+1)]
        dp[1][0]=1
        for i in range(1,m+1):
            for j in range(1, n+1):
                if obs[i-1][j-1]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m][n]