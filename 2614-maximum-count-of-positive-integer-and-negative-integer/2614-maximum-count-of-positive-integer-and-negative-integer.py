class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # posCt=0
        # negCt=0
        # for n in nums:
        #     if n<0:
        #         negCt+=1
        #     if n>0:
        #         posCt+=1
        # return max(negCt, posCt)
        neg=self.bin_search(nums, 0)
        pos=len(nums)-self.bin_search(nums,1)
        return max(neg, pos)
    def bin_search(self, nums, target):
        l,r=0, len(nums)-1
        res=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            else:
                res=m
                r=m-1
        return res
        
        