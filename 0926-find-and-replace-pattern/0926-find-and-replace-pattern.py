class Solution:
    def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
        def f(w):
            m={}
            return [m.setdefault(c, len(m)) for c in w]
        fp=f(p)
        return [w for w in words if f(w)==fp]
