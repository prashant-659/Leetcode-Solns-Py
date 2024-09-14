class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp=[0]*(amount+1)
        # dp[0]=1
        # for c in coins:
        #     for i in range(c,amount+1):
        #         if i-c>=0:
        #             dp[i]+=dp[i-c]
            
        # return dp[amount]  
        # amt=[i for i in range(len(coins))]
        dp=[[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=1
        for i in range(amount+1):
            dp[0][i]=0
        
        for i in range(1,len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
