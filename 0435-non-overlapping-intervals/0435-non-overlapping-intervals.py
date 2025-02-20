class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # start=[x[0] for x in intervals]
        # end=[x[1] for x in intervals]
        count=0
        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:

            if start>=prevEnd:
                prevEnd=end
            else:
                count+=1
                prevEnd=min(end, prevEnd)
        return count