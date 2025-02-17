class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ct=Counter(tiles)

        def backtrack():
            res=0
            for c in ct:
                if ct[c]>0:
                    ct[c]-=1
                    res+=1
                    res+=backtrack()

                    ct[c]+=1
            return res
                


        return backtrack()
