class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum_=0
        ans=0
        l=0
        for r in range(len(nums)):
            sum_+=nums[r]
            while  sum_*(r-l+1)>=k:
                # ans+=1
                sum_ =sum_ - nums[l]
                # prefix
                l+=1
            # if l<=r and (prefix[r]-prefix[l-1])*(r-l+1)<k:
            ans+=r-l+1
        return ans