class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum_=nums[0]
        max_=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                sum_+=nums[i]
                max_=max(sum_,max_)
            else:
                sum_=nums[i]
                max_=max(sum_,max_)
            
        return max_