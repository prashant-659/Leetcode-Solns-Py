class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        mp={}
        for k, v in pick:
            if k not in mp:
                mp[k]={}
            if v not in mp[k]:
                mp[k][v]=0
            mp[k][v]+=1

        winners=0
        for i in range(n):
            if i in mp:
                for c in mp[i].values():
                    if c>i:
                        winners+=1
                        break
        return winners

        