class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # l=set()
        # for i in nums:
        #     if i in l:
        #         return True
        #     l.add(i)
        # return False













        set1=set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return True
            set1.add(nums[i])
        return False
