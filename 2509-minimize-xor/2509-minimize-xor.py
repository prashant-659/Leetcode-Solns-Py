class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def  countSetBits(n): 
            count = 0
            while (n): 
                count += n & 1
                n >>= 1
            return count 
        res=0
        count=countSetBits(num2)

        for i in range(32,-1,-1):
            if (num1 & 1<<i) and count>0 :
                count-=1
                res|=(1<<i)
        
        for i in range(32):
            if count>0 and (num1 &(1<<i))==0:
                count-=1
                res|=1<<i
        return res