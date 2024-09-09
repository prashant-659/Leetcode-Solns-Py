class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_1=0
        num_0s=0

        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                num_0s+=1
            while num_0s>k:
                if nums[l]==0:
                    num_0s-=1
                l+=1
            max_1=max(max_1,(r-l+1))
        return max_1