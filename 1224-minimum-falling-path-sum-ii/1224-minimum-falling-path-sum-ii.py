class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N=len(grid)
        # cache={}
        # #O(n^3) TC #O(n^2)
        # def helper(r, c):
        #     if r==N-1:
        #         return grid[r][c]
        #     if (r,c) in cache:
        #         return cache[(r,c)]
        #     res=float("inf")
        #     for next_col in range(N):
        #         if c!=next_col:
        #             res=min(
        #                 res,
        #                 grid[r][c]+helper(r+1, next_col)
        #             )
        #     cache[(r,c)]=res
        #     return res
        # res=float("inf")
        # for c in range(N):
        #     res=min(res, helper(0,c))
        # return res

        dp=grid[0]
        for r in range(1,N):
            next_dp=[float("inf")]*N

            for curr_c in range(N):
                for prev_c in range(N):
                    if prev_c!=curr_c:
                        next_dp[curr_c]=min(
                            next_dp[curr_c], 
                            grid[r][curr_c]+dp[prev_c]
                        )
            dp=next_dp
        return min(dp)
