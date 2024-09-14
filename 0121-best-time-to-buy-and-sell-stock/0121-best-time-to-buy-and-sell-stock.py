class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # curr_prof=0
        # max_prof=0
        # l=0
        # r=1
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         curr_prof=prices[r]-prices[l]
        #         if curr_prof>max_prof:
        #             max_prof=curr_prof
        #     else:
        #         l=r
        #     r+=1

        # return max_prof

        maxm=0
        curr=0
        l,r=0,0
        while r< len(prices):
            if prices[l]<prices[r]:
                curr=prices[r]-prices[l]
                maxm=max(curr, maxm)

            else:
                l=r
            r+=1
        return maxm

