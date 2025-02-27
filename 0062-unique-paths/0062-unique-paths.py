class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans=0
        dp={(0,0):1}
        def move(d,r):
            if d==0 and r==0:
                return 1
            if d<0 or r<0:
                return 0
            if (d,r) in dp:
                return dp[(d,r)]
            up=move(d-1,r)
            left=move(d, r-1)
            dp[(d,r)]=up+left
            return dp[(d,r)]
        move(m-1,n-1)
        return dp[(m-1,n-1)]
