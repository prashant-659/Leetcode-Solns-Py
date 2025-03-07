class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # dp = [True] * (right + 1)
        # dp[0] = dp[1] = False
        
        # for p in range(2, int(right**0.5) + 1):
        #     if dp[p]:
        #         for multiple in range(p * p, right + 1, p):
        #             dp[multiple] = False
        
        # primes = [p for p in range(left, right + 1) if dp[p]]
        
        # num1, num2 = -1, -1
        # min_diff = float('inf')
        
        # for i in range(len(primes) - 1):
        #     if primes[i + 1] - primes[i] < min_diff:
        #         num1, num2 = primes[i], primes[i + 1]
        #         min_diff = primes[i + 1] - primes[i]
        
        # return [num1, num2] if num1 != -1 else [-1, -1]
        #Sieve

        def get_primes():
            is_Prime=[True]*(right+1)

            is_Prime[0]=is_Prime[1]=False

            for n in range(2, int(sqrt(right))+1):
                if not is_Prime[n]:
                    continue
                for m in range(n+n, right+1,n):
                    is_Prime[m]=False
            primes=[]

            for i in range(len(is_Prime)):
                if is_Prime[i] and i>=left:
                    primes.append(i)
            return primes
        primes=get_primes()
        
        
        
        
        
        
        
        primes=get_primes()
        res=[-1,-1]
        diff=right-left+1
        for i in range(1, len(primes)):
            if primes[i]-primes[i-1] <diff:
                diff=primes[i]-primes[i-1]
                res=[primes[i-1],primes[i]]
        return res