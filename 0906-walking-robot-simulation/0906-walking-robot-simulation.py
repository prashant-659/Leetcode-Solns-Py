class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=y=0
        direct=[[0,1],[1,0],[0,-1],[-1,0]]
        d=0
        res=0
        obstacles={tuple(o) for o in obstacles} #set comprehension
        for i in range(len(commands)):
            
            if commands[i]==-1:
                d=(d+1)%4

            elif commands[i]==-2:
                d=(d-1)%4
            else:
                dx,dy=direct[d]
                for _ in range(commands[i]):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x,y=x+dx,y+dy

            res=max(res,x**2+y**2)
        return res
            
