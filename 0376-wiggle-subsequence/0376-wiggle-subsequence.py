class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        even=1
        odd=1
        for i in range(1,len(nums)):
            if nums[i-1]-nums[i]>0:
                even=odd+1
            elif nums[i-1]-nums[i]<0:
                odd=even+1
                
        return max(even,odd)

                