class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        no=0
        res=0
        while n:
            no=n%10
            n=n//10
            if num%no==0:
                res+=1
        return res
            
