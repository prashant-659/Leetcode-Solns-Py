class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        
        def find_min(nums):
            mini=nums[0]
            miniInd=0
            for i in range(len(nums)):
                if nums[i]<mini:
                    mini=nums[i]
                    miniInd=i
            return miniInd
        for i in range(k):
            x=find_min(nums)
            nums[x]*=multiplier
        return nums






















        
        


        return res