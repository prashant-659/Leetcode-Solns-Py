# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         mp=defaultdict(int)
#         mp[0]=1 # seen already
#         cum_xor=0

#         res=0
#         for ch in word:
#             shift=ord(ch)-ord("a")
#             #1<<sdhift <-binaryshift of ch
#             cum_xor^=(1<<shift)

#             res+=mp[cum_xor] #alll characters are even in count
#             for i in range(10):
#                 check_Xor=cum_xor^(1<<shift)
#                 res+=mp[check_Xor] #check with everycharatcer
#             mp[cum_xor]+=1
#         return res

from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        cum_xor = 0
        result = 0

        for ch in word:
            shift = ord(ch) - ord('a')
            cum_xor ^= (1 << shift)
            result += mp[cum_xor]

            for ch1 in range(10):  # Iterate over 'a' to 'j'
                check_xor = cum_xor ^ (1 << ch1)
                result += mp[check_xor]

            mp[cum_xor] += 1

        return result

                