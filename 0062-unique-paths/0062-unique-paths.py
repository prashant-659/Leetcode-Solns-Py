from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ans=0
        # dp={(0,0):1}
        # def move(d,r):
        #     if d==0 and r==0:
        #         return 1
        #     if d<0 or r<0:
        #         return 0
        #     if (d,r) in dp:
        #         return dp[(d,r)]
        #     up=move(d-1,r)
        #     left=move(d, r-1)
        #     dp[(d,r)]=up+left
        #     return dp[(d,r)]
        # move(m-1,n-1)
        # return dp[(m-1,n-1)]
        dp=[[0] *(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(n+1):
            dp[0][i]=1
        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
