class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # N=len(matrix)
        # cache={}
        # def dfs(r,c):
        #     if r==N:
        #         return 0
            
        #     if c<0 or c==N:
        #         return float("inf")
        #     if (r, c) in cache:
        #         return cache[(r,c)]
        #     res=matrix[r][c]+min(
        #         dfs(r+1,c-1),
        #         dfs(r+1,c),
        #         dfs(r+1,c+1)
        #     )

        #     cache[(r,c)]=res
        #     return res

        
        # res=float("inf")
        # for c in range(N):
        #     res=min(res,dfs(0,c))
        
        # return res

        N=len(matrix)

        for r in range(1,N):
            for c in range(N):
                mid=matrix[r-1][c]
                left=matrix[r-1][c-1] if c>0 else float("inf")
                right=matrix[r-1][c+1] if c<N-1 else float("inf")

                matrix[r][c]=matrix[r][c]+min(mid, left, right)
        return min(matrix[-1])

