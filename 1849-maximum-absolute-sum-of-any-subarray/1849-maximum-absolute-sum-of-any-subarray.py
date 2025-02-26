class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur=0
        maxi=-math.inf
        for n in nums:
            cur=max(cur,0)
            cur+=n
            maxi=max(cur, maxi)
        cur=0 
        max2=math.inf
        for n in nums:
            cur=min(cur, 0)

            cur+=n
            max2=min(cur, max2)
        return max(maxi, abs(max2))
        
            