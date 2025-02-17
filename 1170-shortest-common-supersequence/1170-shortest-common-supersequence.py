class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        dp=[[0 for j in range((n+1))] for i in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        i,j=m,n
        s=[]
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                s.append(str1[i-1])
                i-=1
                j-=1
            else:

                if dp[i][j-1]>dp[i-1][j]:
                    s.append(str2[j-1])
                    j-=1
                else:
                    s.append(str1[i-1])
                    i-=1
        while i>0:
            s.append(str1[i-1])
            i-=1
        while j>0:
            s.append(str2[j-1])
            j-=1
        s.reverse()
        return "".join(s)