class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # r=s[::-1]
        # for i in range(len(s)+1):
        #     if s.startswith(r[i:]):
        #         return r[:i] +s
        def longestSubStringFromStart(s:str):
            if len(s)==0 or len(s)==1:
                return s
            i=len(s)
            while i>0:
                if s[:i]==s[:i][::-1]:
            
                    return s[:i],i
                    break
                i-=1
        if len(s)==1 or len(s)==0:
            return s
        index = longestSubStringFromStart(s)[1]
        adds = s[index:][::-1]
        new = adds +s
        return new 