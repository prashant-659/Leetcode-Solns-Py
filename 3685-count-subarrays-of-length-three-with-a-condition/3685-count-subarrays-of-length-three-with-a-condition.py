class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ct=0
        for i in range(2,len(nums)):
            if nums[i-1]==(nums[i-2]+nums[i])*2:
                ct+=1
        return ct