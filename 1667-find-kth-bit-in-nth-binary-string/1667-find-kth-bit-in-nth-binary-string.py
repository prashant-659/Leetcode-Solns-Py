class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.findK(n, k, False)

    def findK(self, n, k, r):
        if n==1:
            return '1' if r else '0'
        l = 2**n
        if k==(l//2):
            return '0' if r else '1'
        if k < (l//2):
            return self.findK(n-1, k, r)
        else:
            return self.findK(n-1, l-k, not r)