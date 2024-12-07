class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_div(max_balls):
            ops=0
            for n in nums:
                ops+=ceil(n/max_balls)-1
                if ops>maxOperations:
                    return False
            return True
        res=0
        #O(logm *n)

        l=1
        r=max(nums)
        while l<r:
            m=l+((r-l)//2)
            if can_div(m):
                r=m
            else:
                l=m+1
            
        return l