class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        robot1=[0]*(len(grid[0]))
        topRow=sum(grid[0])
        bottomRow=0
        ans=float("inf")
        for i in range(len(grid[0])):
            topRow-=grid[0][i]
            ans=min(ans,max(topRow,bottomRow))
            bottomRow+=grid[1][i]
        return ans
        
            
            


        
