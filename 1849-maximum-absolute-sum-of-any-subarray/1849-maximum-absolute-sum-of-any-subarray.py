class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur=0
        maxi=-math.inf
        cur2=0 
        max2=math.inf
        for n in nums:
            cur=max(cur,0)
            cur+=n
            maxi=max(cur, maxi)

            cur2=min(cur2, 0)

            cur2+=n
            max2=min(cur2, max2)
        
            
        return max(maxi, abs(max2))
        
            