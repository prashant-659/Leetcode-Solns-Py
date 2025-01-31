class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit=set()
        def checkbounds(r,c):
            return (r<0 or c<0 or r==N or c==N)
        
        #1. Preconpute areas
        size=defaultdict(int)
        label=2

        def dfs(r,c, label):
            if checkbounds(r,c) or grid[r][c]==0 or grid[r][c]==label:
                return 0
            grid[r][c]=label

            size=1
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]

            for nr, nc in nei:
                size+=dfs(nr, nc, label)
            return size
        

        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    size[label]=dfs(r,c, label)
                    label+=1

        # tru flpiing ovber
        def connect(r,c):
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            visit=set()
            res=1
            for nr, nc in nei:
                if not checkbounds(nr, nc) and grid[nr][nc] not in visit:
                    res+=size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res


        res=0 if not size else max(size.values()) #[[1,1],[1,1]] for this reasin
        for r in range(N):
            for c in range(N):
                if grid[r][c]==0:
                    res=max(res,connect(r,c))
        return res

