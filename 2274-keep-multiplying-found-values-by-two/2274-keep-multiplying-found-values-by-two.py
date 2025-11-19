class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for n in nums:
            if original in set(nums):
                original*=2
            else:
                break
        return original
            