class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count=1
        repeat=len(b)//len(a)
        while count<=repeat+2:
            if b in a*count:
                return count
            else:
                count+=1
                
        return -1