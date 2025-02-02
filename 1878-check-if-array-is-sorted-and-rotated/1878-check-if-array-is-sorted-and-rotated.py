class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            new=nums[i:]+nums[:i]
            if new==sorted(nums):
                print(new)
                return True

        return False