class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # d=0
        # res=0
        
        # for c in range(len(values[0])-1, -1,-1):
        #     column = [row[c] for row in values]
        #     heapify(column)
        #     while column:
        #         d+=1
        #         res+=d*heappop(column)
        # return res

        m = len(values)
        n = len(values[0])
        heap = []
        for i in range(m):
            heappush(heap, (values[i][-1], i, n - 1))
        
        total_spending = 0
        d = 1
        
        while heap:
            val, i, j = heappop(heap)
            total_spending += val * d
            d += 1
            if j > 0:
                heappush(heap, (values[i][j - 1], i, j - 1))
        
        return total_spending

            