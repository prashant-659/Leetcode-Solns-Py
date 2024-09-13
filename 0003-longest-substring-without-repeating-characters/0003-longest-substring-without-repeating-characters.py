class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        maxm=-0
        cset=set()
        while j<len(s):
            while s[j] in cset:
                cset.remove(s[i])
                i+=1
            
            cset.add(s[j])
            
            maxm=max(maxm,j-i+1)
            j+=1
        return maxm
            
                


           

        
        
        
        
        
        
        
        
        
        
        
        
        
        # charSet=set()

        # l=0
        # res=0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l+=1
        #     charSet.add(s[r])
        #     res=max(res,r-l+1)
        # return res