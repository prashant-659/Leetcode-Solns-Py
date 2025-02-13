class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)>=k:
            return 0
        # if len(nums)==2 and min(nums)>=k:
        #     return 0

        heapify(nums)
        op=0
        while len(nums)>=2:
            
            x=heappop(nums)
            y=heappop(nums)
            if x>=k and y>=k:
                return op
            new=x*2+y
            heappush(nums,new)
            op+=1
        return op

            

