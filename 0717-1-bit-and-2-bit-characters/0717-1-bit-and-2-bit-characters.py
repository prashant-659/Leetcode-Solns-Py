class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        i=0
        one_bit=False
        while i<n:
            if bits[i]==1:
                i+=2
                one_bit=False
            else:
                i+=1
                one_bit=True
        return one_bit