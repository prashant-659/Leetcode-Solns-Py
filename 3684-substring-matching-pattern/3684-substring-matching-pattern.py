class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = p.find("*")
        j = s.find(p[:i])
        return j >= 0 and p[1+i:] in s[j+i:]