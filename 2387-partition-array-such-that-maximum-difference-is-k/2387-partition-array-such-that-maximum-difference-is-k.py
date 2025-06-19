class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        l=0
        ans=0
        for r in range(1,len(nums)):
            if nums[l]-nums[r]>k:
                ans+=1
                l=r
        return ans+1