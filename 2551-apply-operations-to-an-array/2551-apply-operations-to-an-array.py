class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                
        temp = []
        zeros = []
        a=nums
        for i in range(len(a)):
            if a[i] !=0:
                temp.append(a[i])
            else:
                zeros.append(a[i])
        return (temp+zeros)
            
        # ct=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[ct]=nums[i]
        #         ct+=1
        # while ct<len(nums):
        #     nums[ct]=0
        # return nums