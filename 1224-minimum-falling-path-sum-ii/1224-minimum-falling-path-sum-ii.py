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

        # dp=grid[0]
        # for r in range(1,N):
        #     next_dp=[float("inf")]*N

        #     for curr_c in range(N):
        #         for prev_c in range(N):
        #             if prev_c!=curr_c:
        #                 next_dp[curr_c]=min(
        #                     next_dp[curr_c], 
        #                     grid[r][curr_c]+dp[prev_c]
        #                 )
        # #     dp=next_dp
        # # return min(dp) #O(n^3)
        # res=float("inf")
        
        # def getMintwo(row):
        #     two_smallest=[]#(val, idx)


        #     for val, idx in row:
        #         if len(two_smallest)<2:
        #             two_smallest.append((val,idx))
        #         elif two_smallest[1][0]>val:
        #             two_smallest.pop()
        #             two_smallest.append((val, idx))
        #         two_smallest.sort()
        #     return two_smallest

        #     N= len(grid)
        #     first_row=[(val, idx) for idx, val in enumerate(grid[0])]

        #     dp=getMintwo(first_row)

        #     for r in range(1,   N):
        #         next_dp=[] #(val, idx)
        #         for curr_c in range(N):
        #             curr_val=grid[r][curr_c]
        #             min_val=float("inf")

        #             for prev_val, prev_c in dp:
        #                 if curr_c!=prev_c:
        #                     min_val=min(min_val, curr_val+prev_val) 
        #             next_dp.append((min_val, curr_c))
        #             next_dp=getMintwo(next_dp)
        #         dp=next_dp

        #     return min([val for val, idx in dp])
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        res = float("inf")
        
        def getMintwo(row):
            two_smallest = []
            for val, idx in row:
                if len(two_smallest) < 2:
                    two_smallest.append((val, idx))
                elif two_smallest[1][0] > val:
                    two_smallest.pop()
                    two_smallest.append((val, idx))
                two_smallest.sort()
            return two_smallest
        
        N = len(grid)
        first_row = [(val, idx) for idx, val in enumerate(grid[0])]
        dp = getMintwo(first_row)
        
        for r in range(1, N):
            next_dp = []
            for curr_c in range(N):
                curr_val = grid[r][curr_c]
                min_val = float("inf")
                for prev_val, prev_c in dp:
                    if curr_c != prev_c:
                        min_val = min(min_val, curr_val + prev_val) 
                next_dp.append((min_val, curr_c))
            next_dp = getMintwo(next_dp)
            dp = next_dp
        
        return min([val for val, idx in dp])
