class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp=defaultdict(int)
        for i in range(len(s)):
            mp[s[i]]+=1
        for i in range(len(t)):
            mp[t[i]]-=1
        for val in mp.values():
            if val!=0:
                return False
        return True