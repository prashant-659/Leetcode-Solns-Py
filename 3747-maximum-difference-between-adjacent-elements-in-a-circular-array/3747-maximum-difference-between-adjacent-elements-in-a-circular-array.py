class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff=-1
        for i in range(1, len(nums)):
            diff=max(diff, abs(nums[i]-nums[i-1]))
        diff=max(diff, abs(nums[-1]-nums[0]))
        return diff