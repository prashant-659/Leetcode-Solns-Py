class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c=Counter(s)
        ct=0
        for val in c.values():
            if val%2!=0:
                ct+=1
        if ct<=k<=len(s):
            return True
        return False