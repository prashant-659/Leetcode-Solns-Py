class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        last_buy=[float('-inf')]*n
        last_sell=[0]*n
        for i in range(len(prices)):
            last_sell[i]=max(last_sell[i-1],prices[i]+last_buy[i-1])
            last_buy[i]=max(last_buy[i-1],last_sell[i-2]-prices[i])
        return last_sell[-1]

