class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod=10**9+7
        # dp={}
        # def countways(length):
        #     if length>high:
        #         return 0
        #     if length in dp:
        #         return dp[length]
        #     dp[length]=1 if length>=low else 0
        #     dp[length]+=countways(length+zero)+countways(length+one)
        #     return dp[length]%mod
        # return countways(0)

        dp=Counter({0:1})
        for i in range(1, high+1):
            dp[i]=(dp[i-one]+dp[i-zero])%mod
        return sum(dp[i] for i in range(low, high+1))%mod