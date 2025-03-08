class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            # Base case: out of bounds or no gold
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            # Collect gold from the current cell
            current_gold = grid[row][col]
            # Mark the cell as visited by setting it to 0
            grid[row][col] = 0
            
            # Explore all four directions
            max_gold = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, dfs(row + dr, col + dc))
            
            # Backtrack: restore the cell's gold
            grid[row][col] = current_gold
            
            # Return the total gold collecte
            return current_gold+max_gold
        maxi=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    continue
                maxi=max(maxi, dfs(r,c))
        return maxi 

