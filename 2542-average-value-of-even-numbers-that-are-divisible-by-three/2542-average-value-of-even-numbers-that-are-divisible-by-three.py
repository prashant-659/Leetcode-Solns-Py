class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count=0
        val=0
        for n in nums:
            if n%6==0:
                val+=n
                count+=1
        if not count:
            return 0
        return val//count 