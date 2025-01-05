class Solution:
    def calculateScore(self, s: str) -> int:
        mp=defaultdict(list)
        ans=0
        
        for i,c in enumerate(s):
            index=ord(c)-ord("a")
            key=25-index
            if mp[key]:
                ans+=(i-mp[key].pop()) 
            else:
                mp[index].append(i)
        return ans

