class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
        
        # res=[]

        # dist=[0]*len(points)
        # dis=0
        # mapped=defaultdict()
        
        # for i, (x,y) in enumerate(points):
        #     dist = [(sqrt(pow(x, 2) + pow(y, 2)), i) for i, (x, y) in enumerate(points)]           
            

        # heapq.heapify(dist)
        
        # for i in range(k):
        #     dis, index=heapq.heappop(dist)
        #     res.append(points[index])


        # return res

        