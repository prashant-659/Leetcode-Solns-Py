class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # if "0" not in s and int(s)<=k:
        #     return 2**(len(s)-1)
        # if s[0]=="0":
        #     return 0
        mod=10**9+7
        dp=[-1]*len(s)
        n=len(s)
        def possible(i):
            if i>=len(s):
                return 1
            if s[i]=="0":
                return 0
            if dp[i]!=-1:
                return dp[i]
            res=0
            num=0
            for end in range(i,n):
                num=(num*10)+ord(s[end])-ord("0")
                if num>k:
                    break
                res=(res%mod+(possible(end+1)%mod))%mod
            dp[i]=res
            return dp[i]
        return possible(0)

