class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # robot1=[0]*(len(grid[0]))
        # topRow=sum(grid[0])
        # bottomRow=0
        # ans=float("inf")
        # for i in range(len(grid[0])):
        #     topRow-=grid[0][i]
        #     ans=min(ans,max(topRow,bottomRow))
        #     bottomRow+=grid[1][i]
        # return ans
            
        N=len(grid[0])
        preRow1,preRow2=grid[0].copy(), grid[1].copy()
        
        for i in range(1,N):
            preRow1[i]+=preRow1[i-1]
            preRow2[i]+=preRow2[i-1]
        
        res=float("inf")
        
        for i in range(N):
            top=preRow1[-1]-preRow1[i]
            bottom=preRow2[i-1] if i>0 else 0
            secondRobot=max(top, bottom)
            res=min(res, secondRobot)
        return res

        
        
            
            


        
