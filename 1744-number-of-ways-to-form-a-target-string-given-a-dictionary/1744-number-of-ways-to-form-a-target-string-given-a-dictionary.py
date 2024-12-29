# class Solution:
   


#     def numWays(self, words: List[str], target: str) -> int:
#         dp=[[-1]*(1001) for _ in range(1001)]
#         mod=10e7
#         char_freq=[[0]*26 for _ in range(26)]
#         for i in range(len(words)):
#             for j in range(len(words[i])):  # Use len(words[i]) instead of len(words[0])
#                 cur = words[i][j]
#                 char_freq[j][ord(cur) - ord("a")] += 1


#         def countWays( idx, tpos):
#             mod=int(1e7+7)
            
#             target_size=len(target)
#             word_size=len(words[0])
#             if tpos==target_size:
#                 return 1
#             if idx>=word_size or (word_size-idx<target_size-tpos):
#                 #No match
#                 return 0
#             if dp[idx][tpos]!=-1:
#                 return dp[idx][tpos]
#             cur=target[tpos]
#             ways_not_matching=countWays(idx+1,tpos)
#             ways_by_matching=countWays( idx+1,tpos)%mod

#             total_ways=((ways_not_matching+ char_freq[idx][ord(cur)-ord("a")]*ways_by_matching))%mod
#             dp[idx][tpos]=total_ways
#             return total_ways
            
#         return countWays(0,0)

# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         n=len(target)
#         m=len(words[0])
#         mod = 10000007
#         char_freq = [[0] * 26 for _ in range(m)]  # Match word size
        

#         # Fill frequency array
#         for word in words:
#             for j in range(m):
#                 char_freq[j][ord(word[j])-ord("a")]+=1
#         dp=[[0]*(n+1) for _ in range(m+1)]

#         dp[0][0]=1

#         for i in range(1, m+1):
#             for j in range(n+1):
#                 #skip the current column
#                 dp[i][j]=dp[i-1][j]

#                 #use the current column (only if j>0)
#                 if j>0:
#                     char_idx=ord(target[j-1])-ord("a")
#                     dp[i][j]+=dp[i-1][j-1]*char_freq[i-1][char_idx]
#                     dp[i][j]%=mod
#         return dp[m][n]

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        m, n = len(words[0]), len(target)

        # Step 1: Precompute character frequencies in each column
        freq = [[0] * 26 for _ in range(m)]
        for word in words:
            for i in range(m):
                freq[i][ord(word[i]) - ord('a')] += 1

        # Step 2: Dynamic Programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(n + 1):
                # Case 1: Skip the current column
                dp[i][j] = dp[i - 1][j]

                # Case 2: Use the current column (only if j > 0)
                if j > 0:
                    char_index = ord(target[j - 1]) - ord('a')
                    dp[i][j] += dp[i - 1][j - 1] * freq[i - 1][char_index]
                    dp[i][j] %= MOD

        return dp[m][n]