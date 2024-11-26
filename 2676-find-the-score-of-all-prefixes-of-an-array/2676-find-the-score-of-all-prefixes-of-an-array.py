class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]*2
        uptoMax=nums[0]

        for i in range(1,len(nums)):
            uptoMax=max(uptoMax,nums[i])
            prefix[i]=nums[i]+prefix[i-1]+uptoMax
        return prefix
        

