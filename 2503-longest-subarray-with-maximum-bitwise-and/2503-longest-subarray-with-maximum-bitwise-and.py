class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val=res=curr=0
        for i in range(len(nums)):
            if max_val<nums[i]:
                max_val=nums[i]
                res=curr=0
            if max_val==nums[i]:
                curr+=1
                res=max(curr,res)
            else:
                curr=0
            
               

        return res