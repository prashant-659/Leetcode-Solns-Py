class Solution:
    def integerBreak(self, n: int) -> int:
        # dp=[[0]*(n//2+1) for _ in range(n//2+1)]

        # return dp[0]
        #O(n^2) and O(n) space
        dp={1:1}

        for num in range(2, n+1):
            dp[num]=0 if num==n else num
            for i in range(1,num//2+1):
                val=dp[i]*dp[num-i]
                dp[num]=max(dp[num], val)
        return dp[n]



        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num]=0 if num==n else num
            for i in range(1,num):
                val=dfs(i)*dfs(num-i)
                
                dp[num]=max(dp[num],val)
            return dp[num]
        return dfs(n)