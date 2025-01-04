class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n=len(nums)
        prefix=Counter()
        prefix[0]=-1
        best=[0]*n
        running=0
        for index, x in enumerate(nums):
            running+=x
            if index>=1:
                best[index]=best[index-1]
            if running-target in prefix:
                best[index]=max(best[prefix[running-target]]+1, best[index])
            prefix[running]=index
        return best[n-1]