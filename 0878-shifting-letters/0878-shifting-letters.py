class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix=[0]*(len(s))
        res=[]
        prefix[-1]=shifts[-1]
        for i in range(len(s)-2,-1,-1):
            prefix[i]=prefix[i+1]+shifts[i]
        for i in range(len(s)):
            c=(ord(s[i])+prefix[i]- ord("a"))%26 +ord("a")
            st=chr(c)
            res.append(st)
        return  "".join(res)