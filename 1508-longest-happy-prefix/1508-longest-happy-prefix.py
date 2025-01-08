class Solution:
    def longestPrefix(self, s: str) -> str:
        lps=[0]*len(s)
        lps[0]=0
        length=0
        i=1
        while i<len(s):
            if s[i]==s[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                    
                else:
                    lps[i]=0
                    i+=1
        return "".join(s[0:lps[-1]])