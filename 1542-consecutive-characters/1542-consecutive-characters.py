class Solution:
    def maxPower(self, s: str) -> int:
        ct=1
        maxi=-1
        for i in range( len(s)-1):
            if s[i]==s[i+1]:
                ct+=1
                
            else:
                
                ct=1
            maxi=max(ct, maxi)
        return maxi if maxi>1 else 1
