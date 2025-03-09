class Solution:
    MOD = 10**9 + 7

    def modpow(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = (result * a) % self.MOD
            a = (a * a) % self.MOD
            n >>= 1
        return result

    def maximumScore(self, nums, k):
        n = len(nums)
        ma = max(nums)

        # Precompute the biggest prime factor for each number up to ma
        big = [1] * (ma + 1)
        for i in range(2, ma + 1):
            if big[i] == 1:
                for j in range(i, ma + 1, i):
                    big[j] = i

        # Compute prime score for each number in nums
        prime_score = [0] * n
        for i in range(n):
            num = nums[i]
            prev = -1
            while num > 1:
                if big[num] != prev:
                    prime_score[i] += 1
                prev = big[num]
                num //= big[num]

        # Pair each number with its index and sort in descending order
        arr = [(nums[i], i) for i in range(n)]
        arr.sort(reverse=True, key=lambda x: x[0])

        # Find the index of the next strictly greater element with respect to prime score
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and prime_score[i] > prime_score[stack[-1]]:
                right[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # Find the index of the previous greater than or equal to element with respect to prime score
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_score[i] >= prime_score[stack[-1]]:
                left[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # Calculate the total number of subarrays (for debugging)
        total_subarrays = 0
        for i in range(n):
            total_subarrays += (i - left[i]) * (right[i] - i)
        assert total_subarrays == (n * (n + 1)) // 2

        # Compute the result
        result = 1
        for num, ind in arr:
            if k == 0:
                break
            count = (ind - left[ind]) * (right[ind] - ind)
            used = min(count, k)
            k -= used
            result = (result * self.modpow(num, used)) % self.MOD

        return result