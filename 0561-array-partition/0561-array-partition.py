class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        heapify(nums)
        res=0
        while nums:
            a, b=heappop(nums), heappop(nums)
            res+=a
        return res