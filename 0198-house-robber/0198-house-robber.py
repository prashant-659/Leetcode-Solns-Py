class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(len(nums)+1)
        dp[1]=nums[0]
        for i in range(1,n):
            dp[i+1]=max(dp[i],dp[i-1]+nums[i])
        return dp[len(nums)] 