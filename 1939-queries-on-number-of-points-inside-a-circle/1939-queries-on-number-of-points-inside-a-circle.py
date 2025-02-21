class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res=[]
        for x1,y1,r in queries:
            num=0
            for x, y in points:
                if (x-x1)**2 +(y-y1)**2<=r**2:
                    num+=1
            res.append(num)
        return res

            
            