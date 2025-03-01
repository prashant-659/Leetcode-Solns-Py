class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            x=nums[l]
            y=nums[r]
            if y==target-x:
                return [l+1, r+1]
            elif y>target-x:
                r-=1
            else:
                l+=1