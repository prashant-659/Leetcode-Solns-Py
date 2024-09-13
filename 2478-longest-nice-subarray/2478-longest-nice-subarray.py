class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i=0
        AND=0
        res=0
        for j in range(len(nums)):
            while AND & nums[j]:
                AND^=nums[i]
                i+=1
            AND|=nums[j]
            res=max(res,j-i+1)
        return res
