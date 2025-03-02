class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        pu=bounds[0][0]
        pv=bounds[0][1]
        for i in range(1,len(original)):
            diff=original[i]-original[i-1]

            pu=max(pu+diff, bounds[i][0])
            pv=min(pv+diff, bounds[i][1])

            if pu>pv:
                return 0
        return pv-pu+1
            
            
        
            