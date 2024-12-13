class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums=[1]+nums+[1]
        # n=len(nums)
        # dp=[[-1]*(n) for _ in range(n)]

        # def dfs(i,j):
        #     if i>j:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     max_coin=0
        #     for k in range(i,j+1):
        #         gain = nums[i-1]*nums[k]*nums[j+1]

        #         remaining=dfs(i,k-1) +gain +dfs(k+1,j)

        #     dp[i][j]=max_coin
        

        # return dfs(1,n-2)

        nums=[1]+nums+[1]
        dp={}

        def dfs(l, r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            

            dp[(l, r)]=0
            for i in range(l, r+1):
                coins= nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                dp[(l,r)]=max(dp[(l, r)], coins)
            return dp[(l,r)]
            

        
        return dfs(1, len(nums)-2)
