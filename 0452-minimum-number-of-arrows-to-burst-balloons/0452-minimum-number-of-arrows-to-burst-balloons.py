class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        start=points[0][1]
        ans=1
        for i in range(1,len(points)):
            if points[i][0]<=start:
                if start>points[i][1]:
                    start=points[i][1]
            else:
                ans+=1
                start=points[i][1]

        return ans
                