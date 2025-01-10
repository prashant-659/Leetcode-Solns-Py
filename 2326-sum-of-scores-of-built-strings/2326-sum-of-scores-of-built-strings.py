class Solution:
    def sumScores(self, s: str) -> int:
        lps=[0]*len(s)
        dp=[1]*len(s)
        i=1
        length=0
        n=len(s)
        while i<n:
            if s[i]==s[length]:
                dp[i]+=dp[length]
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        return sum(dp)
        