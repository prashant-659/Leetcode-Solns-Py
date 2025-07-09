class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        pre=[endTime[0]-startTime[0]]
        n=len(startTime)
        res=0
        for i in range(1,n):
            pre.append(pre[-1]+endTime[i]-startTime[i])
        for i in range(k-1, n):
            l=endTime[i-k] if i-k>=0 else 0
            r=startTime[i+1] if i+1<n else eventTime
            total_duration=pre[i]-(pre[i-k] if i-k>=0 else 0)
            res=max(res, r-l-total_duration)
        return res
