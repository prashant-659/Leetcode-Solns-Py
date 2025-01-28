class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n=len(nums)

    
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        if k == 0:
            return 0  # though per problem statement, k is positive
        
        max_m = n - 1
        # Precompute factorial and inverse factorial
        fact = [1] * (max_m + 1)
        for i in range(1, max_m + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (max_m + 1)
        inv_fact[max_m] = pow(fact[max_m], MOD-2, MOD)
        for i in range(max_m - 1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Precompute sum_c
        sum_c = [0] * n
        sum_c[0] = 1  # m=0, sum C(0,0) =1
        for m in range(1, n):
            if m < k - 1:
                sum_c[m] = (sum_c[m-1] * 2) % MOD
            else:
                # Compute C(m-1, k-1)
                a = m - 1
                b = k - 1
                if a < b:
                    term = 0
                else:
                    term = fact[a] * inv_fact[b] % MOD
                    term = term * inv_fact[a - b] % MOD
                sum_c[m] = (2 * sum_c[m-1] - term) % MOD
                if sum_c[m] < 0:
                    sum_c[m] += MOD
        
        total = 0
        for i in range(n):
            a = nums[i]
            max_contrib = a * sum_c[i] % MOD
            m = n - i - 1
            min_contrib = a * sum_c[m] % MOD
            total = (total + max_contrib + min_contrib) % MOD
        
        return total
