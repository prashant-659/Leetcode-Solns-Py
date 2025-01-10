class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=1
        length=0
        lps=[0]*len(s)
        n=len(s)
        while i<n:
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
        pattern_len=n-lps[n-1]
        return pattern_len!=n and n%pattern_len==0