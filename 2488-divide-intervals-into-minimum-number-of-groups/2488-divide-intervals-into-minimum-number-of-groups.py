class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])

        res,ct=0,0
        s,e=0,0
        while s<len(intervals):
            if start[s]<=end[e]:
                s+=1
                ct+=1
            else:
                e+=1
                ct-=1

            res=max(res,ct)
        return res
