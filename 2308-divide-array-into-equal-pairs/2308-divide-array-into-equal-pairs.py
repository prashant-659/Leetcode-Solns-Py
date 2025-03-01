class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp=Counter(nums)
        for val in mp.values():
            if val%2!=0:
                return False
        return True