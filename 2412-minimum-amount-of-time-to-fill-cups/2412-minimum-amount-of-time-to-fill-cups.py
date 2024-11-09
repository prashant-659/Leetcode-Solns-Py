import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap=[-a for a in amount]
        heapq.heapify(heap)
        time=0
        while heap[0]!=0:
            ele1=heappop(heap)
            ele2=heappop(heap)

            if ele1!=0: ele1+=1
            if ele2!=0: ele2+=1

            heappush(heap, ele1)
            heappush(heap,ele2)

            time+=1
        return time

                

