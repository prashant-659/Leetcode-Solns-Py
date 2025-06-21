class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        mp=Counter(word)
        res=len(word)
        for val in mp.values():
            y=0
            for val2 in mp.values():
                if val>val2:
                    y+=val2
                elif val2>val+k:
                    y+=val2-(val+k)
            res=min(res, y)
        return res
