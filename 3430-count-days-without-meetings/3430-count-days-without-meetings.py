class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        merged = []
        meetings.sort()
        for interval in meetings:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        ans=0
        for i in range(1, len(merged)):
            prev_end=merged[i-1][1]
            cur_start=merged[i][0]
            ans+=(cur_start-prev_end-1)
        startdekh=min(merged)
        if startdekh[0]>1:
            ans+=startdekh[0]-1
        enddekh=max(merged)
        if days>enddekh[1]:
            ans+=(days-enddekh[1])
        return ans



