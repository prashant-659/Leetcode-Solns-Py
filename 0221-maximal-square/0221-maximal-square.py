class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        max_size=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+int(matrix[i-1][j-1])
                else:
                    dp[i][j]=0
                max_size=max(max_size, dp[i][j])
        return max_size*max_size
