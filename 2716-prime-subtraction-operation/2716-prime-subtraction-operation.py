class Solution:
    def isPrime(self, x: int) -> bool:
        if x==1:
            return False
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    def primeSubOperation(self, nums: List[int]) -> bool:
        p=0
        for n in nums:
            if n<=p:
                return False
            prime=n-p-1
            while prime>0 and not self.isPrime(prime):
                prime-=1
            if prime==0:
                p=n
            else:
                p=n-prime
        return True

