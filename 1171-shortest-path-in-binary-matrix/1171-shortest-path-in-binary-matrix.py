class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        N=len(grid)
       
        q=deque([(0,0, 1)])
        visit=set()
        dir=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        
        while q:
            r,c, path=q.popleft()
            if r==N-1 and c==N-1:
                return path
            for dr,dc in dir:
                nr,nc=r+dr,c+dc
                if nr<0 or nr==N or nc<0 or nc==N or (nr,nc) in visit or grid[nr][nc]==1:
                    continue
                q.append((nr,nc, path+1))
                visit.add((nr,nc))
        return -1