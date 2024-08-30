class Solution:
    def getSum(self, a: int, b: int) -> int:
        # while b!=0:
        #     temp= (a&b)<<1
        #     a=a^b
        #     b=temp
        # return a


        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a