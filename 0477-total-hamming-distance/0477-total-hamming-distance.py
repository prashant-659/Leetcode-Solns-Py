class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=[0]*64
        for num in nums:
            i=0
            while num:
                cnt[i]+=(num&1)
                num=num>>1
                i+=1
        ans=0
        for i in range(32):
            ans+=cnt[i]*(n-cnt[i])
        return ans