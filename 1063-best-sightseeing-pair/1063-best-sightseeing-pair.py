class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # n=len(values)
        # dp=[0]*(n)
        # dp2=[0]*n
        # max_score=float("-inf")
        # for i in range(n):
        #     dp[i]=i+values[i]
        #     dp2[i]=values[i]-i
        # for i in range(n):
        #     max_val
        # return max(dp)+max(dp2)

        
        res=0
        cur_max=values[0]-1
        for i in range(1, len(values)):
            res=max(res,values[i]+cur_max)
            cur_max=max(cur_max-1, values[i]-1)
        return res