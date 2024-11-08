from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_perms = set(permutations(nums))
        return [list(perm) for perm in unique_perms]
