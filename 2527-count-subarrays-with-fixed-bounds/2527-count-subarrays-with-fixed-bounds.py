class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i=-1
        minpos=-1
        maxpos=-1
        ct=0
        ans=0
        j=0
        while j<len(nums):
            if nums[j]<minK or nums[j]>maxK:
                i=j
            if nums[j]==minK:
                minpos=j
            if nums[j]==maxK:
                maxpos=j
            ct=min(minpos,maxpos)-i
            ans+=max(ct,0)
            j+=1
        return ans


