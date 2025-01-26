class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sumleft=0
        sumright=0
        part=0
        for i in range(1,len(nums)):
            sumleft=sum(nums[0:i])
            sumright=sum(nums[i:len(nums)])
            if not (sumright-sumleft)&1:
                part+=1
        return part