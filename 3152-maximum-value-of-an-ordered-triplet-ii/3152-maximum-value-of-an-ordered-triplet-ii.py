class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        suff=[0]*len(nums)
        suff[-1]=nums[-1]
        for i in range(len(nums)-2, -1,-1):
            suff[i]=max(nums[i],suff[i+1])
        pre=[0]*len(nums)
        pre[0]=nums[0]
        for i in range(1,len(nums)):
            pre[i]=max(nums[i],pre[i-1])
        maxi=0
        for i in range(1,len(nums)-1):
            maxi=max(maxi, (pre[i-1]-nums[i])*suff[i+1])
        return maxi

