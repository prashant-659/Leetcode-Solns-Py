class Solution:
    def reverseWords(self, s: str) -> str:
        p=""*len(s) #Let's take leet
        spl=s.split(" ")
        for i in range(len(s)):
            p+=spl[i][::-1]
            if i==len(spl)-1:
                return p
            p+=" "
        
        
            
