class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp=defaultdict(int)
        l=0
        count=0
        for r in range(len(s)):
            mp[s[r]]+=1

            while len(mp)==3:
                count+=(len(s)-r)
                mp[s[l]]-=1
                if mp[s[l]]==0:
                    del mp[s[l]]
                l+=1
                      
        return count