# class Solution:
   
#     def maximumLength(self, s: str) -> int:
#         n=len(s)
#         last_seen="*"
#         winLen=0

#         top3_freq = [[[-1] * 3 for _ in range(26)] for _ in range(2)]  # 2 rows for optimization
#         for i, cur in enumerate(s):
#             idx=ord(s[i])-ord("a")
#             winLen=1 if cur!=last_seen else winLen+1
#             last_seen=cur

#             if winLen>top3_freq[i%2][idx][2]:
#                 top3_freq[i%2][idx][2]=winLen
#                 top3_freq[i % 2][idx].sort(reverse=True)
#         maxlen=-1
#         for row in top3_freq:
#             for top3 in row:
#                 maxlen=max(maxlen, min(top3))
#         return maxlen

class Solution:
    def maximumLength(self, st: str) -> int:
        from collections import defaultdict
        mps = defaultdict(int)
        count = 0
        
        for i in range(len(st)):
            count = 1
            mps[(st[i], count)] += 1

            for j in range(i, len(st)):
                if j + 1 < len(st) and st[j] == st[j + 1]:
                    count += 1
                    mps[(st[i], count)] += 1
                else:
                    break
        
        ans1 = 0
        for key, value in mps.items():
            if value >= 3:
                ans1 = max(ans1, key[1])
        
        return ans1 if ans1 != 0 else -1


