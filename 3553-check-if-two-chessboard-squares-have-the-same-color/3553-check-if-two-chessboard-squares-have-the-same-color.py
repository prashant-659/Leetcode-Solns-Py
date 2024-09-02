class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1=ord(coordinate1[0])-ord('a')
        d1=ord(coordinate2[0])-ord('a')

        c2=ord(coordinate1[1])-1
        d2=ord(coordinate2[1])-1

        return (c1+d1) %2==(c2+d2)%2

        
            
        