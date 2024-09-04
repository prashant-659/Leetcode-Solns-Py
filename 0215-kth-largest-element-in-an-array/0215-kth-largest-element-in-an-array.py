class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums=sorted(nums)
        # return nums[len(nums)-k]
        for i in range(len(nums)):
            nums[i]=-1*nums[i]
        heapq.heapify(nums)
        ele=0
        for i in range(k):
            ele=heapq.heappop(nums)
        return ele*-1
        