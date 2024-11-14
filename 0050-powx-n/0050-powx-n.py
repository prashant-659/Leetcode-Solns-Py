class Solution:
    def myPow(self, x: float, n: int) -> float:





        def formula(base=x, exp=abs(n)):
            if exp==0:
                return 1
            elif exp%2==0:
                return formula(base*base, exp//2)
            else:
                return base *formula(base*base, (exp-1)//2)
        f=formula()
        return float(f) if n>=0 else 1/f