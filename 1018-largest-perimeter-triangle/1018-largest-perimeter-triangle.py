class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        def valid(a,b,c):
            if a+b>c and b+c>a and a+c>b:
                return a+b+c
            return -1
        maxi=float("-inf")
        for i in range(2,len(nums)):
            a=nums[i-2]
            b=nums[i-1]
            c=nums[i]
            maxi=max(maxi,valid(a,b,c))
        return maxi if maxi!=-1 else 0

