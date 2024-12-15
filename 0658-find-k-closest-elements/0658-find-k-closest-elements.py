class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i, c in enumerate(arr):
            heap.append((abs(c-x), c))
        heapify(heap)

        ans=[]

        for i in range(k):
            diff, c =heapq.heappop(heap)
            ans.append(c)
        ans.sort()
        return ans
        