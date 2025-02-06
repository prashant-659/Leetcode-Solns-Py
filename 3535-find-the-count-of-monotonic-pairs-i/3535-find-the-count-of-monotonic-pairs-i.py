class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = 2001
        MOD = 10**9 + 7
        n = len(nums)
        dp = [1] * N  # Initialize dp array with 1s

        for i in reversed(range(n)):
            new_dp = [0] * N
            # Compute the prefix sums of the current dp array
            prefix = [0] * N
            prefix[0] = dp[0]
            for j in range(1, N):
                prefix[j] = (prefix[j-1] + dp[j]) % MOD
            
            for prv1 in range(N):
                if i > 0:
                    prv2 = nums[i-1] - prv1
                else:
                    prv2 = 10**18  # A very large number to avoid negative checks for i=0
                
                if prv2 < 0:
                    break  # Further prv1 will only make prv2 more negative
                
                l = max(prv1, nums[i] - prv2)
                r = nums[i]
                
                if l <= r:
                    if l > 0:
                        total = (prefix[r] - prefix[l-1]) % MOD
                    else:
                        total = prefix[r] % MOD
                    # Ensure non-negative result
                    new_dp[prv1] = (total + MOD) % MOD
                # else remains 0, which is already initialized
            
            dp = new_dp
        
        return dp[0] % MOD