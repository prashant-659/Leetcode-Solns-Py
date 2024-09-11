class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k%=(n-1)*2
        return k if k<n else 2*n-k-2
