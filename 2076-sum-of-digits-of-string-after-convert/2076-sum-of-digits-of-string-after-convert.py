class Solution:
    def getLucky(self, s: str, k: int) -> int:
        asc=""
        for i,c in enumerate(s):
            asc+=(str(ord(c)-ord("a")+1))
        

        while k>0:
            temp=0
            for c in asc:
                temp+=int(c)
            asc=str(temp)
            k-=1
        return int(asc)
        
