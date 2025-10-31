class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dupset=set()
        res=[]
        for i in range(len(nums)):
            if nums[i] in dupset:
                res.append(nums[i])
            dupset.add(nums[i])
        return res