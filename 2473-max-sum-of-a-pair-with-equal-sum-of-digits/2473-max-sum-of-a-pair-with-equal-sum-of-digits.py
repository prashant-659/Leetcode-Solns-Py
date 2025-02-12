class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        def getdigits(n):
            sum_=0
            while n:
                dig=n%10
                sum_+=dig
                n=n//10
            return sum_
        
        mp=defaultdict(int)
        max_sum=-1
        for i, n in enumerate(nums):
            dig=getdigits(n)
            if dig in mp:
                max_sum=max(max_sum, n+mp[dig])
                if mp[dig]<n:
                    mp[dig]=n
            else:
                mp[dig]=n
        return max_sum

