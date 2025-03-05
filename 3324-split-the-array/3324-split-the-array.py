class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mp=Counter(nums)
        for v in mp.values():
            if v>2:
                return False
        return True