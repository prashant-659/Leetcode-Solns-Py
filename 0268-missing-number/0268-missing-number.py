class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums) 
        #XOR operations of a number with 0 will return the number
        # A^A=0, A^0=A, 1^2=1^2
        ans=0
        for i in range(1,n+1):
            ans^=i
        for num in nums:
            ans^=num
        return ans
        

