class Solution:
    def minLength(self, s: str) -> int:

        m=2
        s1=[]
        for c in s:
            if s1 and s1[-1]+c in("AB","CD"):
                s1.pop()
            else:
                s1.append(c)
        return  len(s1)