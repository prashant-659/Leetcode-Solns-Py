class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        line_sweep=[]
        for e in events:
            start=e[0]
            end=e[1]
            val=e[2]
            line_sweep.append((start,1,val))
            line_sweep.append((end+1,-1,val))
        line_sweep.sort()
        max_val=0
        max_seen=0

        for l in line_sweep:
            point=l[0]
            status=l[1]
            val=l[2]

            if status==1:
                max_val=max(max_val, max_seen+val)
            if status==-1:
                max_seen=max(max_seen, val)
        return max_val
