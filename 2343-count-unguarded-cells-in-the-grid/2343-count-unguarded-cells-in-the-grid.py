class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        seen=set()
        R=len(guards)
        C=len(guards[0])

        mat=[[0] *n for _ in range(m)]
        #0=free, 1=guard. 2=wall, 3=guardable


        for r, c in guards:
            mat[r][c]=1
        for r, c in walls:
            mat[r][c] =2

        def mark_guarded(r,c):
            for row in range(r+1,m):
                if mat[row][c] in [1,2]:
                    break
                mat[row][c] = 3

            for row in reversed(range(0,r)):
                if mat[row][c] in [1,2]:
                    break
                mat[row][c] = 3
            
            for col in range(c+1, n):
                if mat[r][col] in [1,2]:
                    break
                mat[r][col]=3

            for col in reversed(range(0, c)):
                if mat[r][col] in [1,2]:
                    break
                mat[r][col]=3
            

        for r,c in guards:
            mark_guarded(r,c)
        
        res=0
        for row in mat:
            for n in row:
                if n==0:
                    res+=1
        return res
        