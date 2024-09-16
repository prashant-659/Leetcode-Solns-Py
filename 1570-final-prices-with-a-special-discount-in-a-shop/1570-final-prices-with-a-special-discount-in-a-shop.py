class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #nearest smaller element to the left/right
        n=len(prices)
        stack=[]
        res=[]
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                res.append(prices[i])
            if len(stack)>0 and stack[-1]<=prices[i]:
                res.append(prices[i]-stack[-1])
            if len(stack)>0 and stack[-1]>prices[i]:
                while len(stack)>0 and stack[-1]>prices[i]:
                    stack.pop()
                if len(stack)==0:
                    res.append(prices[i])
                else:
                    res.append(prices[i]-stack[-1])
            stack.append(prices[i])
        return res[::-1]
            