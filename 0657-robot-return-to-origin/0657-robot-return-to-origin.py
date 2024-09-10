class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c_u,c_d,c_l,c_r=0,0,0,0
        for s in moves:
            if s=="U":
                c_u+=1
            if s=="D":
                c_d+=1
            if s=="R":
                c_r+=1
            if s=="L":
                c_l+=1
        return (c_r==c_l) and(c_u==c_d)