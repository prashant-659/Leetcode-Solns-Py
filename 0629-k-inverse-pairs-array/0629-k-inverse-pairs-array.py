class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod=10**9+7
        # cache={} #n:k
        # def count(n,k):
        #     if n==0:
        #         return 1 if k==0 else 0

        #     if k<0:
        #         return 0
        #     if (n, k) in cache:
        #         return cache[(n,k)]

        #     cache[(n,k)]=0

        #     for i in range(n):
        #         cache[(n,k)]=(cache[(n,k)]+count(n-1, k-i))%mod
            
        #     return cache[(n,k)]
        

        # return count(n,k) #tlc

        prev=[0]*(k+1)
        prev[0]=1

        for N in range(1, n+1):
            cur=[0]*(k+1)
            total=0 #slidng window
            for K in range(k+1):
                if K >=N:
                    total-=prev[K-N]
                total=(total+prev[K])%mod
                cur[K]=total

            prev=cur
        return prev[k]


            
