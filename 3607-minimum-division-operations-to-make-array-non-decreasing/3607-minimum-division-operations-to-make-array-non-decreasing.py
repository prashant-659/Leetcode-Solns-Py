class Solution:
    def minOperations(self, nums: List[int]) -> int:
        import math
        n=len(nums)

        if n==1:
            return 0
        op=0
        def gcd(num):
            if num<=3:
                return 1
            for i in range(2,int(math.sqrt(num))+1):
                if num%i==0:
                    return num//i
            return 1
        r=n-1
        for l in range(n-2,-1,-1):
            if nums[l]>nums[r]:
                nums[l]//=gcd(nums[l])
                op+=1
                if nums[l]>nums[r]:
                    return -1
            r-=1
        return op