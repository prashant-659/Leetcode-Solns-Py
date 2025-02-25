class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        def heap(nums, limit):
            nonlocal ans
            for i,n in enumerate(nums):
                nums[i]=-nums[i]
            heapify(nums)
            for i in range(limit):
                ans.append(-1*heapq.heappop(nums))
        ans=[]
        for i in range(len(grid)):
            heap(grid[i], limits[i])
        ans.sort(reverse=True)
        return sum(ans[:k])
            
                
