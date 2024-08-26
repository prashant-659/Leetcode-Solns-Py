class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=0
        r=1
        while r<len(nums):
            nums[l],nums[r]=nums[r],nums[l]
            l+=2
            r+=2
        return nums