class Solution:
    def check(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     new=nums[i:]+nums[:i]
        #     if new==sorted(nums):
        #         print(new)
        #         return True
        N=len(nums)
        count=1
        if N==1:
            return True
        for i in range(1,N*2):
            if nums[(i-1)%N]<=nums[i%N]:
                count+=1
            else:
                count=1
            if count==N:
                return True
            
                

        return False