class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)%k==0:
            return 0
        return sum(nums)%k