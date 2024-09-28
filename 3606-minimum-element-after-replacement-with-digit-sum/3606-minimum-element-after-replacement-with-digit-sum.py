class Solution:
    def minElement(self, nums: List[int]) -> int:
        minm=float('inf')
        for num in nums:
            add=0

            while num>0:
                add=add+num%10
                num//=10
            minm=min(minm,add)
            
        return minm