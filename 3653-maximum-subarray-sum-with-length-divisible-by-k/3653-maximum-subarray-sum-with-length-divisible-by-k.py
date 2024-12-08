class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix=[0]*(len(nums)+1)
        
        for i in range(len(nums)): 
            prefix[i+1]=prefix[i]+nums[i]
        res=float("-inf")


        for i in range(k):
            cur=0
            for j in range(i,len(nums)-k+1,k):
                n=prefix[j+k]-prefix[j]

                cur=max(n, cur+n)
                res=max(res,cur)
        return res