class Solution:
    def rob(self, nums: List[int]) -> int:
        curr=0
        prev=0

        for n in nums:
            curr,prev=max(prev+n,curr), curr
        return curr
        
        
        
        
        
        
        
        
        
        
        
        
        # rob1=0
        # rob2=0
        # #DP
        # #[rob1,rob2, n, n+1....]
        # for n in nums:
        #     temp=max(n+rob1,rob2)
        #     rob1=rob2
        #     rob2=temp

        # return rob2
        