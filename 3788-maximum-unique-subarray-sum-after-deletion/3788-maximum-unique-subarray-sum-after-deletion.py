class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<=0:
            return max(nums)
        copied=nums.copy()
        for n in nums:
            if n<0:
                copied.remove(n) 
        for n in nums:
            if copied.count(n)>1:
                copied.remove(n)
        return sum(copied)

