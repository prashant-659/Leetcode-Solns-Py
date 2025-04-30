class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ct=0
        for c in nums:
            s=str(c)
            if len(s)&1==0:
                ct+=1
        return ct
