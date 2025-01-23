class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rowCnt=[0]*len(grid)
        colCnt=[0]*len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rowCnt[i]+=1
                    colCnt[j]+=1
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if rowCnt[i]>1 or colCnt[j]>1:
                        res+=1
        return res