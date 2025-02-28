# class Solution:
#     def strStr(self, h: str, n: str) -> int:
#         if len(n) > len(h):
#             return -1
#         i=1
#         lps=[0]*len(n)
#         length=0
#         while i<len(n):
#             if n[i]==n[length]:
#                 length+=1
#                 lps[i]=length
#                 i+=1
#             else:
#                 if length!=0:
#                     length=lps[length-1]
#                 else:
#                     lps[i]=0
#                     i+=1
#         i,j=0,0
#         m=len(n)
#         res=[]
#         while i <len(h):
#             if h[i]==n[j]:
#                 i+=1
#                 j+=1
#             if j==m:
#                 return i-j
#             elif n[j]!=h[i]:
#                 if j!=0:
#                     j=lps[j-1]
#                 else:
#                     i+=1
#         return -1
class Solution:
    def strStr(self, h: str, n: str) -> int:
        if len(n) > len(h):
            return -1
        
        lps = [0] * len(n)
        length = 0
        i = 1
        while i < len(n):
            if n[i] == n[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        m = len(n)
        n1 = len(h)
        i,j = 0,0
        while i < n1:
            if h[i] == n[j]:
                i += 1
                j += 1
                if (j == m):
                    return i - m
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        
        return -1