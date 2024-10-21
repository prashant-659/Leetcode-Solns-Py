class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # for i, c in  enumerate(s):
        #     if c not in mp:
        #         mp[c]=i
            
        
        def backtrack(i,seen):
            if i==len(s):
                return len(seen)
            cont=0
            for j in range(i+1,len(s)+1):
                sub=s[i:j]
                if sub not in seen:
                    seen.add(sub)
                    cont=max(cont,backtrack(j,seen))

                    seen.remove(sub)
            return cont
            
        return backtrack(0,set())
      