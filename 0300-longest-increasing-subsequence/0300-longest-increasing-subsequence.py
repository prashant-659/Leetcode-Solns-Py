class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS=[1]*len(nums)

        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]<nums[j]:
        #             LIS[i]=max(LIS[i],1+LIS[j])
        # return max(LIS)

        #O(N^2)
        #work our way backwards
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if nums[i]< nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)

