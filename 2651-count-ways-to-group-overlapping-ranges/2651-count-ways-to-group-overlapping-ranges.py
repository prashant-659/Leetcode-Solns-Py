class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        res=0
        ranges.sort(key=lambda x: x[0])
        output=[ranges[0]]
        
                
        
        output=[ranges[0]]
        for start, end in ranges[1:]:
            lastEnd=output[-1][1]

            if start<=lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
        mod=10**9+7
        return pow(2, len(output))%mod
