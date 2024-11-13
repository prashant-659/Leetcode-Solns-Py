class Solution:
    def minimumMoves(self, s: str) -> int:
        move=0
        i=0
        # while i<len(s):
        #     if s[i]=="X" :
        #         i+=2
        #         move+=1
        #     else:
        #         i+=1
        # return move
        length=0
        moves=len(s)-1
        while moves>=0:
            if s[moves]=="X":
                moves-=3
                length+=1
            else:
                moves-=1
        return length   

