class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)+1
        nums=set(nums)
        for i in range(1,n+1):
            if i not in nums:
                return i
        return n


