class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<3:
            return len(s)
        c=Counter(s)
        res=0
        dup=0
        for x in c:
            if c[x]>2:
                dup+=c[x]-(1 if c[x]%2 else 2)
        return len(s)-dup
        


            




