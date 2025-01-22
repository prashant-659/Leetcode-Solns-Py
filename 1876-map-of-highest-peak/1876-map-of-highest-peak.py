class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R=len(isWater)
        C=len(isWater[0])
        #multisourced bfs
        visit=set()
        q=deque()
        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r,c, 0))
                    isWater[r][c]=0
                    visit.add((r,c))
        while q:
            r,c,h=q.popleft()

            nei=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr, nc in nei:
                if nr<0 or nr==R or nc<0 or nc==C or (nr,nc) in visit:
                    continue
                q.append((nr, nc, h+1))
                isWater[nr][nc]=h+1
                visit.add((nr,nc))
        return isWater
