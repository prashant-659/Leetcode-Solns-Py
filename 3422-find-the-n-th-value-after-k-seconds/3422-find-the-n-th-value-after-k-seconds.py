class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        prefix=[1]*n
        mod=1000000007
        for i in range(k):
            for j in range(1,n):
                prefix[j]=(prefix[j]+prefix[j-1])%mod
        return int(prefix[n-1])

