class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # listoT=['equilateral','isoceles','scalene']
        # nums=nums.sort()
        # for i in range(len(nums)):
        #     if (nums[i+2]>nums[i]+nums[i+1]):
        #         if nums[]
        nums=sorted(nums)
        if nums[0] +nums[1]>nums[2] and nums[1] +nums[2]>nums[0] and nums[0] +nums[2]>nums[1]:
            if nums[0]==nums[1]==nums[2]:
                return "equilateral"
            elif nums[0]==nums[1] or nums[1]==nums[2] or nums[0]==nums[2]:
                return "isosceles"
            else: 
                return "scalene"
        else: 
            return "none"
        
            
            