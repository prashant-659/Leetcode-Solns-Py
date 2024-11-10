class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=float("inf")
        
    
        for i in range(len(nums)):
            orval=0
            leng=0
            for j in range(i, len(nums)):
                orval|=nums[j]
                leng+=1
                if orval>=k :
                    ans=min(ans,leng)
        return ans if ans!=float("inf") else -1
