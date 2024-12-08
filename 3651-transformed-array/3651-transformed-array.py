class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        new=[0]*len(nums)
        for i in range(len(nums)):
            new[i]=nums[(i+nums[i])%len(nums)]
        return new
