class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        prefix=0
        # prefix_2=[0]*(len(nums)
        # prefix_2[-1]=nums[-1]
        prefix_2=0

        for i in range(len(nums)-1,-1,-1):
            prefix_2=prefix_2+nums[i]

        for i in range(len(nums)-1):
            prefix+=nums[i]
            prefix_2-=nums[i]
            if prefix>=prefix_2:
                res+=1
        return res