class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(pow(x, 0.5))
        if x<=1:
            return x
        i=0
        j=x
        while i<j:
            m=(i+j)//2
            if m*m==x:
                return m
            elif m*m<x:
                i=m+1
            else:
                j=m
        return i-1



