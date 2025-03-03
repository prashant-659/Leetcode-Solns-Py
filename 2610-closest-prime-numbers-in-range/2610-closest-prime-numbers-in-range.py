class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        dp = [True] * (right + 1)
        dp[0] = dp[1] = False
        
        for p in range(2, int(right**0.5) + 1):
            if dp[p]:
                for multiple in range(p * p, right + 1, p):
                    dp[multiple] = False
        
        primes = [p for p in range(left, right + 1) if dp[p]]
        
        num1, num2 = -1, -1
        min_diff = float('inf')
        
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                num1, num2 = primes[i], primes[i + 1]
                min_diff = primes[i + 1] - primes[i]
        
        return [num1, num2] if num1 != -1 else [-1, -1]