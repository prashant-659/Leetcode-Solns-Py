class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dfs - backtracking bfs
        # dp=[amount+1]*(amount+1)
        # dp[0]=0
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c>=0:
        #             dp[a]=min(dp[a],1+dp[a-c])
        
        # return dp[amount] if dp[amount]!=amount+1 else -1


        # Anyone curious about top to bottom recursion(backtracking with memoization) :
    #    memo = {}
    #    def dfs(amount):
    #         if amount == 0:
    #             return 0
    #         if amount<0:
    #             return float('inf')
    #         if amount in memo:
    #             return memo[amount]
            
    #         memo[amount] = min([1+dfs(amount-c) for c in coins])
    #         return memo[amount]    
    #    minimum = dfs(amount)
    #    return minimum if minimum < float("inf") else -1

    #TOP Down Memoization 

        dp=[[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=0
        for i in range(amount+1):
            dp[0][i]=float('inf')
        
        if len(coins)==1:
            if amount%coins[0]==0:
                return amount//coins[0]
            else:
                return -1
        
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')

        for i in range(1,len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return -1 if dp[len(coins)][amount] ==float('inf') else dp[len(coins)][amount]