class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr=intervals[0]
        ct=0
        for i in intervals[1:]:
            if i[0]==curr[0] or i[1] <=curr[1]:
                ct+=1
                curr[1]=max(curr[1],i[1])
            else:
                curr=i
        return len(intervals)-ct