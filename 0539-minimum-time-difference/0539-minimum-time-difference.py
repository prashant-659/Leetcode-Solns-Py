class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            hours, minu=time.split(":")

            min_post_mid=int(hours)*60 + int(minu)
            timePoints[i]=min_post_mid
        timePoints.sort()
        res=1440+timePoints[0]-timePoints[-1]

        for i in range(1,len(timePoints)):
            res=min(res,timePoints[i]-timePoints[i-1])
        return res
