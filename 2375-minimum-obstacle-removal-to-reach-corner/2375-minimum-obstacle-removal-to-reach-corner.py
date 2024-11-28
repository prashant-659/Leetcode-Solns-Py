class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q=[(0,0,0)] #cost, row, col

        #Djikstra's Algorithm


        obs=[[float('inf')]*len(grid[0]) for _ in range(len(grid))] #cost array
        obs[0][0]=0 #first path has cost 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            cost, r,c =heapq.heappop(q)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return cost

            for dr, dc in dir:
                nr, nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]):
                    continue
                new_cost=cost+grid[nr][nc]

                if new_cost<obs[nr][nc]:
                    obs[nr][nc] = new_cost
                    heapq.heappush(q, (new_cost, nr, nc))
        return -1


        #TLE
        # def move(r, c, total, visited):
        #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited:
        #         return float('inf')
        #     if r == len(grid) - 1 and c == len(grid[0]) - 1:
        #         return total
        #     visited.add((r, c))
        #     if grid[r][c] == 1:
        #         total += 1
        #     result = min(
        #         move(r + 1, c, total, visited),
        #         move(r, c + 1, total, visited),
        #         move(r - 1, c, total, visited),
        #         move(r, c - 1, total, visited)
        #     )
        #     visited.remove((r, c))
        #     return result
        
        # return move(0, 0, 0, set())
