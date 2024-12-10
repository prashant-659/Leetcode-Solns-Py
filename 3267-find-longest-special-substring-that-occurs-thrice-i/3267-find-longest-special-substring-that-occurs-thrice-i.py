class Solution:
    def maximumLength(self, s: str)-> int:
        groups=defaultdict(list)
        res=-1
        n=len(s)

        prev=None
        curCount=0

        for c in s + '.':
            if c!=prev:
                if prev!= None:
                    groups[prev].append(curCount)
                    groups[prev]=sorted(groups[prev], reverse=True)[:3]

                prev=c
                curCount=1
            else:
                curCount+=1

        for c in string.ascii_lowercase:
            if c not in groups:
                continue
            
            group_len=groups[c]

            no_of_groups=len(group_len)

            ans=group_len[0]-2

            if no_of_groups==2:
                x, y=group_len

                if y>=x-1:
                    ans=max(ans,x-1)
            elif no_of_groups==3:
                x,y,z=group_len

                if x==y==z:
                    ans=max(ans,x)
                
                elif y>=x-1:
                    ans=max(ans,x-1)
            if ans>0:
                res=max(ans,res)
        return res
                





# # class Solution:
   
# #     def maximumLength(self, s: str) -> int:
# #         n=len(s)
# #         last_seen="*"
# #         winLen=0

# #         top3_freq = [[[-1] * 3 for _ in range(26)] for _ in range(3)]  # 2 rows for optimization
# #         for i, cur in enumerate(s):
# #             idx=ord(s[i])-ord("a")
# #             winLen=1 if cur!=last_seen else winLen+1
# #             last_seen=cur

# #             if winLen>top3_freq[i%2][idx][2]:
# #                 top3_freq[i%2][idx][2]=winLen
# #                 top3_freq[i % 2][idx].sort(reverse=True)
# #         maxlen=-1
# #         for row in range(26):
# #             maxlen=max(maxlen, min(top3_freq[i][0],top3_freq[i][1],top3_freq[i][2]))
# #         return maxlen

# # class Solution:
# #     def maximumLength(self, st: str) -> int:
# #         from collections import defaultdict
# #         mps = defaultdict(int)
# #         count = 0
        
# #         for i in range(len(st)):
# #             count = 1
# #             mps[(st[i], count)] += 1

# #             for j in range(i, len(st)):
# #                 if j + 1 < len(st) and st[j] == st[j + 1]:
# #                     count += 1
# #                     mps[(st[i], count)] += 1
# #                 else:
# #                     break
        
# #         ans1 = 0
# #         for key, value in mps.items():
# #             if value >= 3:
# #                 ans1 = max(ans1, key[1])
        
# #         return ans1 if ans1 != 0 else -1

# # class Solution:
# #     def maximumLength(self, s: str) -> int:
# #         n = len(s)
# #         top3_freq = [[-1] * 3 for _ in range(26)]  # 2 rows for optimization

# #         # Find top-3 substring lengths for each character (a to z)
# #         last_seen = '*'
# #         win_len = 0

# #         for i, curr in enumerate(s):
# #             idx = ord(curr) - ord('a')
# #             win_len = win_len + 1 if curr == last_seen else 1
# #             last_seen = curr

# #             # Efficiently update top3_freq
# #             if win_len > top3_freq[i % 2][idx][2]:
# #                 top3_freq[i % 2][idx][2] = win_len
# #                 top3_freq[i % 2][idx].sort(reverse=True)

# #         # Find the maxLen of substring
# #         max_len = -1
# #         for row in top3_freq:
# #             for top3 in row:
# #                 max_len = max(max_len, min(top3))

# #         return max_len
# # from collections import Counter

# # class Solution:
# #     def maximumLength(self, s: str) -> int:
# #         # Step 1: Find all special substrings
# #         n = len(s)
# #         substr_count = Counter()
        
# #         # Step 2: Generate all special substrings
# #         for i in range(n):
# #             char = s[i]
# #             length = 1
# #             for j in range(i + 1, n):
# #                 if s[j] == char:
# #                     length += 1
# #                     substr_count[char * length] += 1
# #                 else:
# #                     break
        
# #         # Step 3: Find the longest special substring that occurs at least 3 times
# #         max_length = -1
# #         for substring, count in substr_count.items():
# #             if count >= 3:
# #                 max_length = max(max_length, len(substring))
        
# #         return max_length
# from collections import defaultdict

# class Solution:
#     def maximumLength(self, s: str) -> int:
#         n = len(s)
#         freq = defaultdict(lambda: defaultdict(int))  # freq[char][length] = count

#         # Calculate frequencies of substrings
#         last_seen = '*'
#         win_len = 0
#         for i, curr in enumerate(s):
#             win_len = win_len + 1 if curr == last_seen else 1
#             last_seen = curr
#             freq[curr][win_len] += 1

#         # Find the maximum length of substrings occurring at least thrice
#         max_len = -1
#         for char, lengths in freq.items():
#             for length, count in lengths.items():
#                 if count >= 3:
#                     max_len = max(max_len, length)

#         return max_len
