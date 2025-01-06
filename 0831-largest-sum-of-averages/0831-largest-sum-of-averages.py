class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N=len(nums)
        dp={}
        @cache
        def largestSuffix(index, kleft):
            if index==N:    
                if kleft==0:
                    return 0
                return float("-inf")
            if kleft==0:
                return float("-inf")
            if (index, kleft) in dp:
                return dp[(index,kleft)]
            count=0
            curSum=0
            best=0.
            for i in range(index, N):
                curSum+=nums[i]
                count+=1
                best=max(best, curSum/count+largestSuffix(i+1, kleft-1))
            dp[(index, kleft)]=best
            return dp[(index,kleft)]
        
        return largestSuffix(0,k)

        