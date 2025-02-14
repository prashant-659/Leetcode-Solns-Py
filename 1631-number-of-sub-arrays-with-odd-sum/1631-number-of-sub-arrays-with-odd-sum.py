class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        mod=10**9+7
        dp=[0]*n
        dp[0]=arr[0]&1
        for i in range(1, n):
            if arr[i]&1:
                dp[i]=i-dp[i-1]+1 #arrray itself
            else:
                dp[i]=dp[i-1]
        return sum(dp)%mod
            
        