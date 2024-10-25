class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split(" ")
        if len(l)!=len(pattern):
            return False
        mp={}
        mp2={}
        for i in range(len(pattern)):
            if pattern[i] in mp and mp[pattern[i]]!=l[i]:
                return False
            mp[pattern[i]]=l[i]
            if l[i] in mp2 and mp2[l[i]]!=pattern[i]:
                return False
            mp2[l[i]]=pattern[i]
        return True
