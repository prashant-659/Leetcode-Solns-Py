class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap=[]
        for num, start, end in trips:
            heap.append((start, num))
            heap.append((end, -num))
        heapify(heap)

        while  capacity>=0 and heap:
            capacity-=heappop(heap)[1]
        return len(heap)==0
