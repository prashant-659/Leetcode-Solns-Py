class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ct=Counter(s)
        if max(ct.values())==1:
            return 0
        left=set()
        res=set() #middle_c, outerc_c
        for m in s:
            ct[m]-=1
            for c in left:
                if ct[c]>0:
                    res.add((m,c))

            left.add(m)
        
        return len(res)