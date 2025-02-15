class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur=0
        maxSum=-math.inf
        for n in nums:
            cur = max(cur, 0)
            cur += n
            maxSum = max(maxSum, cur)
        cur=0
        for i in reversed(range(len(nums))):
            nums[i]=-nums[i]
        cur=0
        maxSum2=-math.inf
        for n in nums:
            cur = max(cur, 0)
            cur += n
            maxSum2 = max(maxSum2, cur)
        return max(maxSum, maxSum2)
