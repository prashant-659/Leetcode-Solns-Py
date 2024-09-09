class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                submatrix=(
                    grid[r][c],
                    grid[r+1][c],
                    grid[r][c+1],
                    grid[r+1][c+1]
                    )
                if sum([cell=="B" for cell in submatrix])!=2:
                    return True
        return False