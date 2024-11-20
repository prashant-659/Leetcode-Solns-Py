class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r=0,0
        p=1
        res=0
        if k<=1:
            return 0
        while r<len(nums):
            p*=nums[r]
            if p<k:
                res+=r-l+1
            elif p>=k:
                while p>=k:
                    p/=nums[l]
                    l+=1
                res+=r-l+1
            r+=1

        return res         
