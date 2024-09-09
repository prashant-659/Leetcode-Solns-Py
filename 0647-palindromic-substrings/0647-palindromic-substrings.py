class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        for i in range(len(s)):
            res+=self.count_Pali(s,i,i)# for odd len
            res+=self.count_Pali(s,i,i+1) #for even len
        return res
        
    def count_Pali(self, s, l ,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res
            