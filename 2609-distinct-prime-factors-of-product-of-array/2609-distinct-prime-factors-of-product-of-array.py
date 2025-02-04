class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        size=len(nums)
        ans=set()
        for n in nums:
            t=2
            while t*t<=n:
                while n%t==0:
                    n//=t
                    ans.add(t)
                t+=1
            if n>1:
                ans.add(n)

        return len(ans)

        # def prime(n):
        #     i=1
        #     while i<sqrt(n):
        # for n in ans:
            
        