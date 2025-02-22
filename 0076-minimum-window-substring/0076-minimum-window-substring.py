class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_present={}
        for c in t:
            if c not in t_present:
                t_present[c]=1
            else:
                t_present[c]+=1
        count=len(set(t))
        l=0
        minlen=float("inf")
        for r in range(len(s)):
            if s[r] in t_present:
                t_present[s[r]]-=1
                if t_present[s[r]]==0:
                    count-=1
            
            while count==0:
                if s[l] in t_present:
                    t_present[s[l]]+=1
                    if t_present[s[l]]==1:
                        count+=1
                        if (r-l+1)<minlen:
                            minlen=r-l+1
                            start=l
                l+=1
                    
        if minlen==float("inf"):
            return ""
        return s[start: start+minlen]
                    
            
