class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur=0
        cur2=0
        maxSum=-math.inf
        maxSum2=math.inf
        for n in nums:
            cur = max(cur, 0)
            cur += n
            maxSum = max(maxSum, cur)

            cur2 = min(cur2, 0)
            cur2 += n
            maxSum2 = min(maxSum2, cur2)
           
        return max(maxSum, abs(maxSum2))
