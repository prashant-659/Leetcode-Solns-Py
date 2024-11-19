class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mp=Counter(s)
        res=0
        for c in t:
            if c in mp:
                mp[c]-=1
                if mp[c]==0:
                    del mp[c]
        for i in mp.values():
            res+=i
        return res
            