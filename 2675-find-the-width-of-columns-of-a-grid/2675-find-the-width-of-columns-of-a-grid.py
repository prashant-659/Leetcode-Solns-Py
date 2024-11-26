class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        maxwidth=[]
        
        for c in range(len(grid[0])):
            length=0
            maxlen=0
            for r in range(len(grid)):
                length=len(str(grid[r][c]))
                maxlen=max(length,maxlen)
            maxwidth.append(maxlen)
        return maxwidth