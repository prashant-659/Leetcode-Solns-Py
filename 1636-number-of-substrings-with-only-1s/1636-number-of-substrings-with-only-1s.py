class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        ans=0
        count=0
        for i in range(len(s)):
            if s[i]=="1":
                count+=1
                ans+=count
            else:
                count=0
        return ans%mod