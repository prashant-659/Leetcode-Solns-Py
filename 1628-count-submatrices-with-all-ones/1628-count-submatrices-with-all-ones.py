# class Solution:
#     def numSubmat(self, matrix: List[List[int]]) -> int:
#         R=len(matrix)
#         C=len(matrix[0])
#         dp = [[0 for _ in range(C)] for _ in range(R)]
#         for r in range(R):
#             for c in range(C):
#                 if matrix[r][c]:
#                     dp[r][c]=1+dp[r][c-1] if c-1>=0 else 0
#         ans=0
#         for r in range(R):
#             for c in range(C):
#                 rc=math.inf
#                 for k in range(r,-1,-1):
#                     rc=min(rc, dp[k][c])
#                     if rc==0:
#                         break
#                     ans+=rc
#         return ans
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        r, c = len(mat), len(mat[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    dp[i][j] = 1 + (dp[i][j - 1] if j - 1 >= 0 else 0)
        for i in range(r):
            for j in range(c):
                mn = math.inf
                for k in range(i, -1, -1):
                    mn = min(mn, dp[k][j])
                    if mn == 0:break
                    ans += (mn)
        return ans


        