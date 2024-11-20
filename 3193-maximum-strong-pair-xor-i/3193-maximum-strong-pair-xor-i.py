class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=0
        res=0
        while r< len(nums):
            x=nums[l]
            y=nums[r]
            if y-x>x:
                l+=1
                continue
            for i in range(l,r):
                res=max(res,nums[i]^y)
            r+=1
        return res
