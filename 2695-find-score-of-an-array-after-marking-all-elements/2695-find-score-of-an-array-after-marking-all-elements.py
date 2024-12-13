class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[(nums[i], i) for i in range(len(nums))]
        heapify(heap)
        adj=set()
        score=0


        while len(adj)!=len(nums):
            
            ele, i=heapq.heappop(heap)
            if i in adj:
                continue
            score+=ele
            adj.add(i)
            if i-1>=0:
                adj.add(i-1)
            if i+1<len(nums):
                adj.add(i+1)
        return score

            