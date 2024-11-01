class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        res=""
        res+=s[0]
        res+=s[1]
        for i in range(2,len(s)) :
            if s[i]!=res[-1] or s[i]!=res[-2]:
                res+=s[i]
            
                  
        return res