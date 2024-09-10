class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        half_sum=sum(nums)//2
        dp=[[False for _ in range(half_sum+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=True

        for i in range(1,len(nums)+1):
            for j in range(1,half_sum+1):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
        
        # if sum(nums)%2!=0:
        #     return False

        # half_sum=sum(nums)//2
        # dp=[[False for _ in range(len(nums)+1)]for _ in range(half_sum+1)]
        # for i in range(len(nums) + 1):
        #     dp[0][i]=True

        # for i in range(1,half_sum+1):
        #     for j in range(1,len(nums)+1):
        #         if nums[j-1]>i:
        #             dp[i][j]=dp[i][j-1]
        #         else:
        #             dp[i][j] = dp[i - nums[j - 1]][j - 1] or dp[i][j - 1]
        # return dp[half_sum][len(nums)]