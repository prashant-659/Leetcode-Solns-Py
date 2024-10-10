class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        table = [(a, i) for i, a in enumerate(nums)]
        table.sort()

        imin = float("inf")
        res = 0
        for a, i in table:
            res = max(res, i - imin)
            imin = min(imin, i)

        return res
