class Solution:
    def smallestNumber(self, n: int) -> int:
        
        def powerif2(n):
            p=1
            while p<n:
                p*=2
            return p
        return powerif2(n+1)-1