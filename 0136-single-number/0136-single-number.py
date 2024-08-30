class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in range(1,len(nums)):
        #     nums[0]^=nums[i]
        # return nums[0]

        res=0

        for i in range(len(nums)):
            res^=nums[i]
        return res
