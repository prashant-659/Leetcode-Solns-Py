class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans=m=0
        for i in range(len(nums)):
            ans+=m
            m=max(m, nums[i])
        return ans
