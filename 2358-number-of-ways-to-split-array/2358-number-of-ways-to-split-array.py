class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        prefix=0
        prefix_2=[0]*(len(nums))

        prefix_2[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            prefix_2[i]=prefix_2[i+1]+nums[i]
        for i in range(len(nums)-1):
            prefix+=nums[i]
            if prefix>=prefix_2[i+1]:
                res+=1
        return res