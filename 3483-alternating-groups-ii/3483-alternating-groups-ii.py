class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        groups=0
        l=0
        for r in range(1,len(colors)):
            if colors[r]==colors[r-1]:
                l=r
                continue
            if r-l+1>k:
                l=l+1
            if r-l+1==k:
                groups+=1
        return groups


            
