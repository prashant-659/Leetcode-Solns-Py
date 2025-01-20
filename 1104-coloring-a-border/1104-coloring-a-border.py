class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        q=deque()
        m,n=len(grid), len(grid[0])

        visit=set()
        q.append((row,col))
        visit.add((row*n+col))
        ori=grid[row][col]

        nei=[(1,0), (-1,0), (0,1),(0,-1)]
        while q:
            r,c=q.popleft()

            if r==0 or r==m-1 or c==0 or c==n-1:
                grid[r][c]=color
            
            for dr, dc in nei:
                nr, nc=r+dr, c+dc

                if nr<0 or nr>m-1 or nc<0 or nc>n-1 or (nr*n+nc) in visit:
                    continue

                if grid[nr][nc]==ori:
                    q.append((nr, nc))
                    visit.add((nr*n+c))
                else:
                    grid[r][c]=color
        return grid


            
            