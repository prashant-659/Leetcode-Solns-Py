class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        w=list(s)
        l=0
        r=len(w)-1
        res=""
        while l<=r:
            if w[l] in vowels and w[r] in vowels:
                w[l],w[r]=w[r],w[l]
                l+=1
                r-=1
            elif w[l] not in vowels and w[r] in vowels:
                l+=1
            elif w[l] in vowels and w[r] not in vowels:
                r-=1
            else:
                l+=1
                r-=1
        return "".join(w)

