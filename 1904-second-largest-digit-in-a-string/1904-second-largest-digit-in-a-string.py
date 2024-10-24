class Solution:
    def secondHighest(self, s: str) -> int:
        res=set()
        for i in range(len(s)):
            if (ord(s[i])-ord("0"))>=0 and (ord(s[i])-ord("0"))<=9:
                res.add(s[i])
        if len(res)==1 or len(res)==0:
            return -1
        else:
            res=list(res)
            res.sort()
            return int(res[-2])

