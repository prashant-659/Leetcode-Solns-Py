class Solution:
    def minimumSteps(self, s: str) -> int:
        l=0
        count=0
        for r in range(len(s)):
            if s[r]=="0":
                count+=(r-l)
                l+=1


        return count