class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp=Counter(nums)
        for val in mp.values():
            if val&1:
                return False
        return True