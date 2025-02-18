class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        s2=s[::-1]
        dp=[[0 for j in range((n+1))] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        x=dp[n][n]
        return n-x
        # if max(dp)==len(s)+1:
        #     return 0
        # max_=max(dp)
        # return 2*len(s)-max_
            
