class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        # prevEnd=intervals[0][1]
        # prevStart=intervals[0][0]
        # array=[[prevStart,prevEnd]]
        # for i in range(1,len(intervals)):
        #     if intervals[i][0]<=prevEnd:

        #         array.append([prevStart,max(intervals[i][1],prevEnd)])
        #         prevStart=intervals[i][0]
        #         prevEnd=max(intervals[i][1],prevEnd)
            
        #     else:
        #         array.append([intervals[i][0],intervals[i][1]])
        # return array
        output=[intervals[0]]
        for start, end in intervals[1:]:
            lastEnd=output[-1][1]

            if start<=lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
        return output

