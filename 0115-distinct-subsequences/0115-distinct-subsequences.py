class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0]* (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0]=1
        mod=int(1e9+7)
        

        for m in range(1,len(s)+1):
            for n in range(1,len(t)+1):

                if s[m-1]==t[n-1]:
                    dp[m][n]=(dp[m-1][n-1] +dp[m-1][n])%mod
                else:
                    dp[m][n]=(dp[m-1][n])%mod

        
        return dp[m][n]

