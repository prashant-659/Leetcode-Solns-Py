class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R=len(isWater)
        C=len(isWater[0])
        #multisourced bfs
        q=deque()
        res=[[-1] *C for _ in range(R)]
        #enqueue all water cells
        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r,c))
                    isWater[r][c]=0
                    res[r][c]=0
        while q:
            r,c=q.popleft()
            h=res[r][c]

            nei=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in nei:
                if nr<0 or nr==R or nc<0 or nc==C or  res[nr][nc]!=-1:
                    continue
                q.append((nr, nc))
                res[nr][nc]=h+1
                
        return res







