class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # r=s[::-1]
        # for i in range(len(s)+1):
        #     if s.startswith(r[i:]):
        #         return r[:i] +s


        # def longestSubStringFromStart(s:str):
        #     if len(s)==0 or len(s)==1:
        #         return s
        #     i=len(s)
        #     while i>0:
        #         if s[:i]==s[:i][::-1]:
            
        #             return s[:i],i
        #             break
        #         i-=1
        # if len(s)==1 or len(s)==0:
        #     return s
        # index = longestSubStringFromStart(s)[1]
        # adds = s[index:][::-1]
        # new = adds +s
        # return new 

        #TLE - BF
        # def is_Pali(s,l,r):
        #     while l<=r:
        #         if s[l]!=s[r]:
        #             return False
        #         l,r=l+1,r-1
        #     return True
        # for r in reversed(range(len(s))):
        #     if is_Pali(s,0,r):
        #         suffix=s[r+1:]
                
        #         return suffix[::-1]+s
        # return ""

        #rabin karp algo - O(n)
        # hash functions algo
        prefix=0
        suffix=0
        base=29
        last_index=0 #-1
        power=1
        mod=10**9+7

        for i, c in enumerate(s):
            char=(ord(c)-ord("a")+1) #offset by 1 so S starts with 1

            prefix=(prefix * base) %mod
            prefix=(prefix + char) %mod

            suffix=(suffix+char*power)% mod
            power=(power*base) %mod

            if prefix==suffix:
                last_index=i


        suffix=s[last_index+1:]
        return suffix[::-1]+s
