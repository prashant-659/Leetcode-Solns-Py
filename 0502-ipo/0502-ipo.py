class Solution:
    def findMaximizedCapital(self, k: int, w: int, p: List[int], c: List[int]) -> int:
        
        # while min_capital<=w and i< len(c):
        #     min_capital=c[i]
        #     heappush(heap, [-p[i], c[i]])
        #     i+=1
        pc=sorted(zip(c,p))
        heap=[]
        index=0
        for i in range(len(c)):
            if w>=pc[i][0]:
                heapq.heappush(heap,-pc[i][1])
            else:
                index=i
                break
        
        for _ in range(k): 
            
            if heap:
                profit=heappop(heap)
                w+=(-profit)
            while index < len(pc) and pc[index][0] <= w:
                heapq.heappush(heap, -pc[index][1])
                index += 1
        return w
                      
            



