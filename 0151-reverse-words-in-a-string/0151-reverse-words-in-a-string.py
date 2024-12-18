class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()

        s=s.split(" ")
        s=s[::-1]
        ans=[]
        for i,c in enumerate(s):
            s[i]=c.strip()
            if s[i]=="":
                continue
            ans.append(s[i])
        return " ".join(ans)
        
