class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap=[0]

        sweep=[]
        for l, r, h in buildings:
            sweep.append([l, -h])
            sweep.append([r, h])
        sweep.sort()

        ans=[]
        for e, h in sweep:
            if  h<0:
                if h<heap[0]:
                    ans.append([e,-h])
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapify(heap)
                if -h<heap[0]:
                    ans.append([e, -heap[0]])
        return ans
