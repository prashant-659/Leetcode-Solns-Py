class Solution:
    def numSubseq(self, nums: List[int], k: int) -> int:
        nums.sort()
        mod=10**9+7
        l=0
        r=len(nums)-1
        power=[1]*len(nums)
        for i in range(1,len(nums)):
            power[i]=(power[i-1]*2)%mod

        res=0
        while l<=r:
            m=(l+r)//2
            if nums[l]+nums[r]<=k:
                res=(res+power[r-l])%mod
                l+=1
            else:
                r-=1
        return res

        
                