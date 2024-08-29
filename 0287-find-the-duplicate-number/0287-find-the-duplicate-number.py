class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return nums[i]
        # return -1

        #Floyd'sm detection dycle
        slow, fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break #similarto do shile
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
