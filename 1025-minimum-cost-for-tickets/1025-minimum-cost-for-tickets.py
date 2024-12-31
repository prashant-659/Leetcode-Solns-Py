class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp={}
        # def dfs(i):
        #     if i==len(days):
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     dp[i]=float("inf")
        #     j=i
        #     for d, c in zip([1,7,30], costs):
                
        #         while j<len(days) and days[j]<days[i]+d:
        #             j+=1
        #         dp[i]=min(dp[i],c+dfs(j))
        #     return dp[i]
        # return dfs(0)

        dp=[0]*(len(days)+1)

        for i in reversed(range(len(days))):
            j=i
            dp[i]=float("inf")

            for cost, duration in zip(costs,[1,7,30]):
                while j<len(days) and days[j]<days[i]+duration:
                    j+=1
                dp[i]=min(dp[i], cost+dp[j])
        return dp[0]