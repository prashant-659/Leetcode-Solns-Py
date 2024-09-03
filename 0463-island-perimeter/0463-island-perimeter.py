class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        visit=set()
        perimeter=0
        def dfs(r,c):
            if (r<0 or r>=R or
                c<0 or c>=C or
                grid[r][c]==0):
                return 1
            if  (r,c) in visit:
                return 0
            visit.add((r,c))
            

            
            return (dfs(r+1,c)+
                    dfs(r-1,c)+
                    dfs(r,c+1)+
                    dfs(r,c-1))
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    perimeter+=dfs(r,c)
        return perimeter