class Solution:
    def rob(self, nums: List[int]) -> int:
        # curr=0
        # prev=0

        # for n in nums:
        #     curr,prev=max(prev+n,curr), curr
        # return curr
        
        # rob1,rob2=0,0
        # # [rob1,rob2, n, n+1, n+2......] 
        # for n in nums:
        #     temp=max(n+rob1, rob2)
        #     rob1=rob2
        #     rob2=temp
        # return rob2

        #bottom-up
        nums.append(0)
        for i in range(len(nums)-3,-1,-1):
            nums[i]=max(nums[i]+nums[i+2], nums[i+1])
        return max(nums[0],nums[1])
        
        
        
        
        
        
        
        
        
        # rob1=0
        # rob2=0
        # #DP
        # #[rob1,rob2, n, n+1....]
        # for n in nums:
        #     temp=max(n+rob1,rob2)
        #     rob1=rob2
        #     rob2=temp

        # return rob2
        