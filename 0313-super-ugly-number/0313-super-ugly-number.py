class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp=[[0]*(n+1) for _  in range(len(primes)+1)]
        # for i in range(n+1):
        #     dp[0][i]=1
        # for i in range(1,n+1):
        #     for j in range(len(primes)):
        #         if i%primes[j]==0:
        #             dp[i][j]=
        #         else:
        #             continue

        ugly=[1]
        seen=set([1])
        for _ in range(n):
            cur_ugly=heapq.heappop(ugly)
            for prime in primes:
                next_ugly=cur_ugly*prime
                if next_ugly not in seen:
                    heapq.heappush(ugly, next_ugly)
                    seen.add(next_ugly)
        return cur_ugly

         
        return dp[n][len(primes)]