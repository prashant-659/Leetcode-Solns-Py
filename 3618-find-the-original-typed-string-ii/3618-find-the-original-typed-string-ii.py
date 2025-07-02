class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod=10**9+7
        n=len(word)
        groups=[]
        res=1
        cnt=1

        for i in range(1,n):
            if word[i]==word[i-1]:
                cnt+=1
            else:
                groups.append(cnt)
                res=(res*cnt)%mod
                cnt=1

        groups.append(cnt)
        res=(res*cnt)%mod

        if k<=len(groups):
            return res
        #if k > len(groups), perform dp

        dp=[[0]*(k) for _ in range((len(groups)+1))]
        dp[0][0]=1
        for i in range(1, len(groups)+1):
            pref=[0]*k
            pref[0]=dp[i-1][0]
            for idx in range(1, k):
                pref[idx]=pref[idx-1]+dp[i-1][idx]

            for j in range(1, k):
                left=j-1-groups[i-1]
                pre_s=pref[j-1]
                if left>=0:
                    pre_s-=pref[left]
                dp[i][j]=pre_s
        return (res-sum(dp[-1]))%mod















                # for cnt in range(1,groups [i-1]+1):
                #     if j<cnt<0:
                #         break
                #     dp[i][j]+=dp[i-1][j-cnt]

