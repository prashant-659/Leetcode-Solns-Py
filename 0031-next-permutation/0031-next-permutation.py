class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=False
        l=-1
        for i in range(len(nums)-2,-1,-1):
            # l=i-1
           
            if nums[i]>=nums[i+1]: continue
            l=i
            for r in range(len(nums)-1,i,-1):
                if nums[l]<nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                    flag=True
                    break
            break

        nums[l+1:]=reversed(nums[l+1:])
            