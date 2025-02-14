class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x:(x[0],x[1]))
        if len(stockPrices)==1:
            return 0
        res=1
        pre_y=stockPrices[1][1]-stockPrices[0][1]
        pre_x=stockPrices[1][0]-stockPrices[0][0]
        
        for i in range(1, len(stockPrices)-1):
            cur_y=stockPrices[i+1][1]-stockPrices[i][1]
            cur_x=stockPrices[i+1][0]-stockPrices[i][0]
            if pre_y*cur_x!=cur_y*pre_x:
                res+=1
                pre_y=cur_y
                pre_x=cur_x
                
        return res
