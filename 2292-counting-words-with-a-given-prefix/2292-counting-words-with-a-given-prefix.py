class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res=0
        end=len(pref)
        for w in words:
            if w[:end]==pref:
                res+=1
        return res