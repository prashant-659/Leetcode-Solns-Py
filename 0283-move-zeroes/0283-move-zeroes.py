class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ct]=nums[i]
                ct+=1
        while ct<len(nums):
            nums[ct]=0
            ct+=1
        return nums
        