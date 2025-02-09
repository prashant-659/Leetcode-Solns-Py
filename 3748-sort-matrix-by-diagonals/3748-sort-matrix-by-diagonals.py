class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        store=defaultdict(list)
        for r in range(n):
            for c in range(n):
                store[r-c].append(grid[r][c])
            
        for i,v in store.items():
            if i<0:
                store[i].sort(reverse=True)
            else:
                store[i].sort()
        for r in range(n):
            for c in range(n):
                grid[r][c]=store[r-c].pop()
        return grid

                    

        