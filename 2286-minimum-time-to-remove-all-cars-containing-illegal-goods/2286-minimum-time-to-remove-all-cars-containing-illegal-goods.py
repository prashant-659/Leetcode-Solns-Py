# class Solution:
#     def minimumTime(self, s: str) -> int:
#         n=len(s)
#         s2=s[::-1]
#         prefix=[0]*(n)
#         suffix=[0]*(n)
#         prefix[0]=int(s[0])
#         suffix[0]=int(s2[0])
#         t=0
#         for i in range(1,n):
#             t=min(i-t+1,2)

#             if s[i]=="1":
#                 prefix[i]=min(prefix[i-1]+2, i-t+1)
#             else:
#                 prefix[i]=prefix[i-1]
#         t=0
#         for i in range(1,n):
#             t=min(i-t+1,2)

#             if s2[i]=="1":
#                 suffix[i]=min(suffix[i-1]+2, i-t+1)
#             else:
#                 suffix[i]=suffix[i-1]
#         print(prefix,suffix[::-1])
#         suffix=suffix[::-1]
#         # return min((prefix[n-1]+suffix[n-2]), prefix[n-2]+suffix[n-1])
            
#         for i in range(n):
# class Solution:
#     def minimumTime(self, s: str) -> int:
#         n = len(s)
#         if n == 0:
#             return 0
        
#         # Compute prefix array
#         prefix = [0] * n
#         prefix[0] = 1 if s[0] == '1' else 0
#         for i in range(1, n):
#             if s[i] == '1':
#                 prefix[i] = min(prefix[i-1] + 2, i + 1)
#             else:
#                 prefix[i] = prefix[i-1]
        
#         # Compute suffix array
#         suffix = [0] * n
#         suffix[-1] = 1 if s[-1] == '1' else 0
#         for i in range(n-2, -1, -1):
#             if s[i] == '1':
#                 suffix[i] = min(suffix[i+1] + 2, n - i)
#             else:
#                 suffix[i] = suffix[i+1]
        
#         # Find the minimum total time
#         min_time = float('inf')
#         for i in range(n):
#             if i == n-1:
#                 min_time = min(min_time, prefix[i])
#             else:
#                 min_time = min(min_time, prefix[i] + suffix[i+1])
        
#         return min_time
        
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # prefix array (left to right)
        prefix = [0] * n
        prefix[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            if s[i] == '1':
                prefix[i] = min(prefix[i-1] + 2, i + 1)
            else:
                prefix[i] = prefix[i-1]
        
        suffix = [0] * n
        suffix[-1] = 1 if s[-1] == '1' else 0
        for i in range(n-2, -1, -1):
            if s[i] == '1':
                suffix[i] = min(suffix[i+1] + 2, n - i)
            else:
                suffix[i] = suffix[i+1]
        
        min_time = min(prefix[-1], suffix[0])  
        for i in range(n-1):
            min_time = min(min_time, prefix[i] + suffix[i+1])
        
        return min_time