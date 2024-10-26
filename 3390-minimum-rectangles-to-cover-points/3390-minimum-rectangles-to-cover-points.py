class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        res=0
        last=-1
        for x, y in points:
            if x>last:
                res+=1
                last=x+w
             
        return res



        #     if x not in mp:
        #         mp[x]=1
        #     else:
        #         mp[x]+=1
        # return (len(mp)-1)