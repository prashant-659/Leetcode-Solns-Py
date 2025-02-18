class Solution:
    def minInsertions(self, s: str) -> int:
        s2=s[::-1]
        dp=[[0 for j in range((len(s2)+1))] for i in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(s2)+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        x=dp[len(s)][len(s)]
        return len(s)-x
        # if max(dp)==len(s)+1:
        #     return 0
        # max_=max(dp)
        # return 2*len(s)-max_
            
