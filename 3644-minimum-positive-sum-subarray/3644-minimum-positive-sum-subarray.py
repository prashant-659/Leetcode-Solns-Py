class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        n=len(nums)
        min_Sum=float("inf")
        for i in range(l,r+1):
            if i>n:
                continue
            
            window_sum=sum(nums[:i])
            if window_sum>0:
                min_Sum=min(min_Sum, window_sum)
            for j in range(i,n):
                window_sum+=nums[j]-nums[j-i]
                if window_sum>0:
                    min_Sum=min(min_Sum, window_sum)

        return min_Sum if min_Sum  < float('inf') else -1


                    

            
