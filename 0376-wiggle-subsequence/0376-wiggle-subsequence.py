class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        down=1
        up=1
        for i in range(1,len(nums)):
            if nums[i-1]-nums[i]>0:
                down=up+1
            elif nums[i-1]-nums[i]<0:
                up=down+1
                
        return max(up,down)

                