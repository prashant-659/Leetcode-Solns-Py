class Solution:
    def findComplement(self, num: int) -> int:
        # bit_len=num.bit_length()

        # mask=(1<<bit_len)-1
        # return num^mask

        result=0
        power=1
        while num>0:
            result+=(num%2^1)*power
            power<<=1
            num>>=1
        return result