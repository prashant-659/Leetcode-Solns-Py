class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dict_cnt={'a':0,'b':0,'c':0}
        n=len(s)
        l=0
        res=0

        for r in range(len(s)):
            dict_cnt[s[r]]+=1
            while(dict_cnt['a'] and dict_cnt['b']  and dict_cnt['c']):
                res+=n-r
                dict_cnt[s[l]]-=1
                l+=1

        return res
        