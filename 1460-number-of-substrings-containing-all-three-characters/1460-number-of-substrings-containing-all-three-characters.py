class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # mp=defaultdict(int)
        # l=0
        # count=0
        # for r in range(len(s)):
        #     mp[s[r]]+=1

        #     while len(mp)==3:
        #         count+=(len(s)-r) # number of valid substrings ending at index r
        #         mp[s[l]]-=1
        #         if mp[s[l]]==0:
        #             del mp[s[l]]
        #         l+=1
                      
        # return count
        last = {'a': -1, 'b': -1, 'c': -1} 
        count = 0
        
        for j in range(len(s)):
            last[s[j]] = j  
            
            min_last = min(last['a'], last['b'], last['c'])
            
            # If all three characters are , count valid substrings
            if min_last != -1:
                count += (min_last + 1)
        
        return count