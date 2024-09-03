class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max=0
        maxall=0
        for i in range(len(nums)):
            
            if nums[i]==1:
                cur_max+=1
            else:
                cur_max=0
            maxall=max(cur_max,maxall)
        return maxall