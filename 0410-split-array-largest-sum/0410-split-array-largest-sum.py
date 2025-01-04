class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarr=0
            curSum=0
            for n in nums:
                curSum+=n
                if curSum>largest:
                    subarr+=1
                    
                    if subarr+1>k:
                        return False
                    curSum=n
            return True
        
        
        l,r=max(nums), sum(nums)
        res=r

        while l<=r:
            mid=l+((r-l)//2)

            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

