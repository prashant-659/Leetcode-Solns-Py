# class Solution:
#     def isMatch(self,s: str, p: str) -> bool:
#         m, n = len(s), len(p)
        
#         # Initialize the DP table
#         dp = [[False] * (n + 1) for _ in range(m + 1)]
#         dp[0][0] = True  # Both s and p are empty
        
#         # Initialize first row (s is empty)
#         for j in range(1, n + 1):
#             if p[j - 1] == '*':
#                 dp[0][j] = dp[0][j - 2]  # '*' matches zero occurrence of the preceding element
        
#         # Fill the DP table
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 elif p[j - 1] == '*':
#                     dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrence
#                     if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
#                         dp[i][j] = dp[i][j] or dp[i - 1][j]
        
#         return dp[m][n]

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p,s):
            return True
        else:
            return False